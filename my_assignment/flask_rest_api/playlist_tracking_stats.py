import json
import jsonpickle
from json import JSONEncoder
import boto3
import time
import os
import pandas as pd
import numpy as np
import io
from io import StringIO




# permissions
# ---------------------------
# athena:StartQueryExecution
# athena:GetQueryExecution
# athena:GetQueryResults
# glue:GetTable


def lambda_handler(event, context):
    client = boto3.client('athena')
    v_aws_access_key_id = os.environ['V_AWS_ACCESS_KEY_ID']
    v_aws_secret_access_key = os.environ['V_AWS_SECRET_ACCESS_KEY']

	 
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
    
    print('Processing Response')
    
    for row in track_stats_results['ResultSet']['Rows']:
        rows_track_stats.append(row['Data'])

    columns = rows_track_stats[0]
    rows_track_stats = rows_track_stats[1:]
    
    print('value of rows_track_stats', rows_track_stats)

    columns_list = []
    for column in columns:
        columns_list.append(column['VarCharValue'])
        
    print('columns type',type(columns))
    print('columns value',columns)
    print('columns_list value',columns_list)

    dataframe_track_status = pd.DataFrame(columns = columns_list)
    print('data frame value is',dataframe_track_status)

    for row in rows_track_stats:
        df_row = []
        try:
            for data in row:
                df_row.append(data['VarCharValue'])
            # print('before df_row value is',df_row)
            dataframe_track_status.loc[len(dataframe_track_status)] = df_row
            # print('after df_row value is',dataframe_track_status)
        except:
            pass

    df_track_status_op = pd.DataFrame(dataframe_track_status, columns = columns_list)
    print('value of df_track_status_op',df_track_status_op)
    
    # writing track stat output to s3 bucket
    s3 = boto3.client("s3",aws_access_key_id=v_aws_access_key_id,aws_secret_access_key=v_aws_secret_access_key)
    json_buffer = io.StringIO()
    df_track_status_op.to_json(json_buffer, orient='records')
    json_final = json.dumps(jsonpickle.encode(json_buffer.getvalue()), indent = 4)
    json_final.replace('\"','')
    json_buffer.seek(0)
    s3.put_object(Bucket="lambda-func-op",Body=json.loads(json_final),Key='playlist_track_stats.json')