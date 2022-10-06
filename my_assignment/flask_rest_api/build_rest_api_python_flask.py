import json
import csv
import boto3
import base64
import os
import datetime as dt
import flask
# import pandas as pd
# from flask_lambda import FlaskLambda
from flask import Flask, request, jsonify


app = Flask(__name__)

#step1 = normalizing_playlist()
#step2 = playlist_tracking_stats()


@app.route('/<bucket_name>', methods=['GET'])
def get_all_list_items():
        all_items = lambda_handler
        return all_items
		
@app.route('/<bucket_name>/max_value', methods=['GET'])
def get_max_list_items(max_value):
        max_item = lambda_handler[max_value]
        return max_items


@app.route('/<bucket_name>/<key_name>/<playlist_id>', methods=['GET'])
def get_specific_playlist(playlist_id):
    key = {'playlist_id': playlist_id}
    if request.method == 'GET':
        new_playlist = lambda_handler[playlist_id]
        print('value of new playlist is',new_playlist)
        if new_playlist:
            return lambda_handler[playlist_id]
        else:
            return lambda_handler({"message": "playlist not found"}, 404)


@app.route('/<bucket_name>/tracklist/<playlist_id>', methods=['GET'])
def get_track_playlist(playlist_id):
    key = {'playlist_id': playlist_id}
    if request.method == 'GET':
        new_playlist = lambda_handler[playlist_id]
        if new_playlist:
            return lambda_handler[playlist_id]
        else:
            return lambda_handler({"message": "playlist not found"}, 404)

s3 = boto3.client('s3')

def lambda_handler(event, context):

    datestamp = dt.datetime.now().strftime("%Y/%m/%d")
    timestamp = dt.datetime.now().strftime("%s")    
    filename_json = "/tmp/file_{ts}.json".format(ts=timestamp)
    filename_csv = "/tmp/file_{ts}.csv".format(ts=timestamp)
    keyname_s3 = "uploads/output/{ds}/{ts}.json".format(ds=datestamp, ts=timestamp)

    json_data = []
	
	
    bucket_name = event["pathParameters"]["bucket"]
    key_name = event["queryStringParameters"]["file"]
    playlist_id = event["queryStringParameters"]["playlist"]
	
    s3_object = s3.get_object(Bucket=bucket_name, Key=key_name)
	
    data = s3_object["Body"].read()
    contents = data.decode('utf-8')
    

    
    with open(filename_csv, 'a') as csv_data:
        csv_data.write(contents)
    
    with open(filename_csv) as csv_data:
        csv_reader = csv.DictReader(csv_data)
        print('value of csv_reader...',csv_reader)
        for csv_row in csv_reader:
            print('.......test......',csv_row)
            json_data.append(csv_row)
  
    #print('the value of json_data is......',json_data)
    
    '''      
    with open(filename_json, 'w') as json_file:
        json_file.write(json.dumps(json_data))
    
    with open(filename_json, 'r') as json_file_contents:
        response = s3.put_object(Bucket=bucket_name, Key=keyname_s3, Body=json_file_contents.read())
        
    '''
    json_body=json.dumps(json_data)
    print('json body.....', json_body)
    
    json_load=json.loads(json_body)
    print('json loads .....',json_load)
   
    # Soln 1 hardcoded field name
    ''' 
    dic = { x['playlist_id']: x['playlist_name'] for x in json_load}
    print('--------value of d.........', dic[playlist_id])
    print('playlist_id:{} ,playlist_name:{}'.format(playlist_id,dic[playlist_id]))
    '''
    # Sol 2 w/o hardcoding filed name
    dict_op = list(filter(lambda playlist_op : playlist_op['playlist_id']==playlist_id, json_load))
    print('value of dict_op ......',dict_op)
    
    
    if playlist_id in json_body:
        return {
        "statusCode": 200,
        # "headers": {
        #    "Content-Type": "application/json",
        # "Content-Disposition": "attachment; filename={}".format(keyname_s3)
        # },
          "body": json.dumps(dict_op)
        #  ,"isBase64Encoded": True
            }
    else: 
        return 'Unrecognized Playlist ID'
     
    os.remove(filename_csv)
    os.remove(filename_json)