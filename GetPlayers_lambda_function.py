import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('A3_Players')
    response = table.scan()
   
    item = response['Items']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }