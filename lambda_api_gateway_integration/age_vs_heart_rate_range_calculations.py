import json


# API Gateway https://.../<stagename>/<route>?in_age=43
def lambda_handler(event, context):
    #lambda handler function
    #print "handler started"
    str_age = event ["queryStringParameters"]["in_age"]
    age = int(str_age)
    print('input age is', age)
    calculate_max_heart_rate(age)
    calculate_low_heart_rate_range(event,context)
    calculate_high_heart_rate_range(event,context)
    message = 'low:{} and high:{}'.format(round(low_heart_rate_range),round(high_heart_rate_range))
    print('message is',message)
    return {
       # "low": round(low_heart_rate_range),
       # "high":round(high_heart_rate_range)
       # "body": json.dumps(age)
       # "body": json.dumps(round(low_heart_rate_range))
       "body" : message
    }
 
 
def calculate_max_heart_rate(age):
    # calculates maximum heart rate
    global max_heart_rate
    max_heart_rate = 220 - age
    return int(max_heart_rate)
 
def calculate_low_heart_rate_range(event,context):
    # calculates the low heart rate range
    global low_heart_rate_range
    low_heart_rate_range = int(max_heart_rate) * .7
    return low_heart_rate_range
 
def calculate_high_heart_rate_range(event,context):
    # calculates the high heart rate range
    global high_heart_rate_range
    high_heart_rate_range = int(max_heart_rate) * .85
    return high_heart_rate_range
