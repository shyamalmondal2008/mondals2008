import json
import boto3
import time
import os
import pandas as pd
import numpy as np
# import seaborn as sns
import sklearn
from sklearn.preprocessing import MinMaxScaler
from io import StringIO



# permissions
# ---------------------------
# athena:StartQueryExecution
# athena:GetQueryExecution
# athena:GetQueryResults
# glue:GetTable


def lambda_handler(event, context):
    client = boto3.client('athena')
    v_normalization_max = os.environ['NORMALIZATION_MAX']
    v_aws_access_key_id = os.environ['V_AWS_ACCESS_KEY_ID']
    v_aws_secret_access_key = os.environ['V_AWS_SECRET_ACCESS_KEY']
	 
	#setup and perform query
    queryStart = client.start_query_execution(
	        QueryString = "SELECT followed_by,acousticness_avg,acousticness_stdev,artist_followers_avg,artist_followers_stdev,danceability_avg,danceability_stdev,duration_ms_avg,duration_ms_stdev,energy_avg,energy_stdev,instrumentalness_avg,instrumentalness_stdev,liveness_avg,liveness_stdev,mode_avg,mode_stdev,num_unique_artist_first_page,speechiness_avg,speechiness_stdev,tempo_avg,tempo_stdev,valence_avg,valence_stdev FROM playlists;",
            QueryExecutionContext = {
			     'Database': 'assignment_sep_2022'
			},
            ResultConfiguration = {
	              'OutputLocation': 's3://athena-query-result-sep-2022/outpu'	
			
			}
	    )
    #Observe Result
    queryId = queryStart['QueryExecutionId']
    time.sleep(15)
	
    results = client.get_query_results(QueryExecutionId = queryId)
    
    for row in results['ResultSet']['Rows']:
        print(row)
        
        
    results_1 = []
    rows = []
    
    print('Processing Response')
    
    for row in results['ResultSet']['Rows']:
        rows.append(row['Data'])

    columns = rows[0]
    rows = rows[1:]

    columns_list = []
    for column in columns:
        columns_list.append(column['VarCharValue'])
        
    print('Creating Dataframe')

    dataframe = pd.DataFrame(columns = columns_list)
    print('data frame value is',dataframe)

    for row in rows:
        df_row = []
        try:
            for data in row:
                df_row.append(data['VarCharValue'])
            # print('before df_row value is',df_row)
            dataframe.loc[len(dataframe)] = df_row
            # print('after df_row value is',dataframe)
        except:
            pass
    scaler = MinMaxScaler()
    df_normalizer = scaler.fit_transform(dataframe)
    print('type of df_normalizer is .........',type(df_normalizer))
    print('value of df_normalizer is ..........',df_normalizer)

    df_normalizer_op = pd.DataFrame(df_normalizer, columns = ['followed_by','acousticness_avg','acousticness_stdev','artist_followers_avg','artist_followers_stdev','danceability_avg','danceability_stdev','duration_ms_avg','duration_ms_stdev','energy_avg','energy_stdev','instrumentalness_avg','instrumentalness_stdev','liveness_avg','liveness_stdev','mode_avg','mode_stdev','num_unique_artist_first_page','speechiness_avg','speechiness_stdev','tempo_avg','tempo_stdev','valence_avg','valence_stdev'])

    print('data type of df_normalizer_op',type(df_normalizer_op))
    df_normalizer_op_new =  df_normalizer_op * int(v_normalization_max)
    print('value of df_normalizer_op_new.......',df_normalizer_op_new)
    
    # calculation of average of numeric values
    df_average_all_values = df_normalizer_op_new.mean(numeric_only = True)
    df_average_series_to_frame = df_average_all_values.rename(None).to_frame().T
    print('average values',df_average_series_to_frame)
    print('data types average values',type(df_average_series_to_frame))
    
    # writing normalizer output to s3 bucket
    s3 = boto3.client("s3",aws_access_key_id=v_aws_access_key_id,aws_secret_access_key=v_aws_secret_access_key)
    csv_buffer = StringIO()
    df_normalizer_op_new.to_csv(csv_buffer, header=True, index=False)
    csv_buffer.seek(0)
    s3.put_object(Bucket="lambda-func-op",Body=csv_buffer.getvalue(),Key='playlists_normalized.csv')
    
    # writing average output to s3 bucket
    s3_avg = boto3.client("s3",aws_access_key_id=v_aws_access_key_id,aws_secret_access_key=v_aws_secret_access_key)
    csv_avg_buffer = StringIO()
    df_average_series_to_frame.to_csv(csv_avg_buffer, header=True, index=False)
    csv_avg_buffer.seek(0)
    s3_avg.put_object(Bucket="lambda-func-op",Body=csv_avg_buffer.getvalue(),Key='playlists_average.csv')
    
    