import json
import boto3
import time
import os
import pandas as pd
import numpy as np
# import seaborn as sns
import sklearn
from sklearn.preprocessing import MinMaxScaler



# permissions
# ---------------------------
# athena:StartQueryExecution
# athena:GetQueryExecution
# athena:GetQueryResults
# glue:GetTable


def lambda_handler(event, context):
    client = boto3.client('athena')

	 
	#setup and perform query
    queryStart = client.start_query_execution(
	        QueryString = "SELECT playlist_id,track_id FROM playlist_tracks WHERE playlist_id='37i9dQZF1DX4LE3mRVj255';",
            QueryExecutionContext = {
			     'Database': 'assignment_sep_2022'
			},
            ResultConfiguration = {
	              'OutputLocation': 's3://athena-query-result-sep-2022/playlists'	
			
			}
	    )
    #Observe Result
    queryId = queryStart['QueryExecutionId']
    time.sleep(10)
    results = client.get_query_results(QueryExecutionId = queryId)
    
    # setup and perform query ---for track_stats
    
    track_stats_queryStart = client.start_query_execution(
	        QueryString = "SELECT * FROM playlist_tracks_stats;",
            QueryExecutionContext = {
			     'Database': 'assignment_sep_2022'
			},
            ResultConfiguration = {
	              'OutputLocation': 's3://athena-query-result-sep-2022/playlists'	
			
			}
	    )
    #Observe Result ---for track_stats
    track_stats_queryId = track_stats_queryStart['QueryExecutionId']
    time.sleep(15)  
    track_stats_results = client.get_query_results(QueryExecutionId = track_stats_queryId)
    
    rows_track_stats = []
    for track_row in track_stats_results['ResultSet']['Rows']:
        rows_track_stats.append(track_row['Data'])
    json_rows_track_stats = json.dumps(rows_track_stats)
    print('value of json_rows_track_stats is', json_rows_track_stats)
    

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
    print('value of data frame is',dataframe)
    json_out_put = dataframe.to_json()
    print('json_out_put value is',json_out_put)
    print('type of json_out_put value is',type(json_out_put))
    # json location ,'s3://lambda-func-op/playlist_tracks_stats.json'