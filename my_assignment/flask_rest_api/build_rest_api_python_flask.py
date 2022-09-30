import json
import csv
import boto3
import base64
import os
import datetime as dt
import flask
# from flask_lambda import FlaskLambda
from flask import Flask, request, jsonify


app = Flask(__name__)

# Invoke Step 1 & Step2
step1 = normalizing_playlist()
step2 = playlist_tracking_stats()

@app.route('/<bucket_name>', methods=['GET'])
def get_all_list_items():
        all_items = lambda_handler
        return all_items
		
@app.route('/<bucket_name>/max_value', methods=['GET'])
def get_max_list_items(max_value):
        max_item = lambda_handler[max_value]
        return max_items


@app.route('/<bucket_name>/playlist/<playlist_id>', methods=['GET'])
def get_specific_playlist(playlist_id):
    key = {'playlist_id': playlist_id}
    if request.method == 'GET':
        playlist = lambda_handler[playlist_id]
        if playlist:
            return lambda_handler[playlist_id]
        else:
            return lambda_handler({"message": "playlist not found"}, 404)


@app.route('/<bucket_name>/tracklist/<playlist_id>', methods=['GET'])
def get_track_playlist(playlist_id):
    key = {'playlist_id': playlist_id}
    if request.method == 'GET':
        playlist = lambda_handler[playlist_id]
        if playlist:
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
	
	
    bucket_name = event ["pathParameters"]["bucket"]
    key_name = event ["queryStringParameters"]["file"]
    #playlist_id = event ["queryStringParameters"]["in_playlist_id"]
	
    s3_object = s3.get_object(Bucket=bucket_name, Key=key_name)
	
    data = s3_object["Body"].read()
    contents = data.decode('utf-8')
    
    with open(filename_csv, 'a') as csv_data:
        csv_data.write(contents)
    
    with open(filename_csv) as csv_data:
        csv_reader = csv.DictReader(csv_data)
        for csv_row in csv_reader:
            json_data.append(csv_row)
            
    with open(filename_json, 'w') as json_file:
        json_file.write(json.dumps(json_data))
    
    with open(filename_json, 'r') as json_file_contents:
        response = s3.put_object(Bucket=bucket_name, Key=keyname_s3, Body=json_file_contents.read())
    
    #json_dumps = json.dumps('{bucket}/{key}'.format(bucket=bucket_name,key=keyname_s3))
    #file_content = json_dumps.read()

    return {
        "statusCode": 200,
        "headers": {
        "Content-Type": "application/json",
        "Content-Disposition": "attachment; filename={}".format(keyname_s3)
         },
        "body": json.dumps(json_data),
        "isBase64Encoded": True
    }
    
    os.remove(filename_csv)
    os.remove(filename_json)