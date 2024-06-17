import json
import csv
import boto3

from io import StringIO
from datetime import datetime

def lambda_handler(event, context):
    
    catalog = event.get('catalog')
    createDate = event.get('createDate')
    if not catalog or not createDate:
        return {
            'statusCode':400,
            'body':json.dumps('missing required parameter')
        }
    table_name = 'test_data'
    bucket_name = 'bucket2024-5-29'
    csv_file_name = 'dynamodb_data.csv'
    
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
    
    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    
    if items:
        header = items[0].keys()
        csv_writer.writerow(header)
    
        for item in items:
            csv_writer.writerow(item.values())
    
    s3.put_object(Bucket=bucket_name, Key=csv_file_name, Body=csv_buffer.getvalue())
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully exported data to s3://{bucket_name}/{csv_file_name}')
    }