import json

import boto3
from datetime import date
from datetime import datetime
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)  
        return super().default(o)
    
def lambda_handler(event, context):
    
    catalog = int(event["queryStringParameters"]['catalog'])
    createDate = event["queryStringParameters"]['createDate']
    
   
    if not catalog or not createDate:
        return {
            'statusCode':400,
            'body':json.dumps('missing required parameter')
        }
    table_name = 'test_data'
    bucket_name = 'bucket_2024-5-29'

    
    dynamodb = boto3.resource('dynamodb')
    s3 = boto3.client('s3')
    
    table = dynamodb.Table(table_name)
    
    response = table.scan(FilterExpression="#catalog = :catalog AND createDate > :createDate",
        ExpressionAttributeNames={"#catalog": "catalog"},
        ExpressionAttributeValues={
            ":catalog": catalog,
            ":createDate": createDate
        })
    items = response['Items']
    
    
   
    
    http_re = {}
    http_re['statusCode'] = 200
    http_re['headers'] = {}
    http_re['headers']['Content-Type'] = 'application/json'
    http_re['body'] =  json.dumps(items, cls=DecimalEncoder)
   
    return http_re