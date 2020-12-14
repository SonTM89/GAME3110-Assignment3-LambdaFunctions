import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('A3_Players')
    
    if event["queryStringParameters"]['player_id'] and event["queryStringParameters"]['player_name'] and event["queryStringParameters"]['exp'] and event["queryStringParameters"]['lvl']:
        table.put_item(
           Item={
                'player_id': event["queryStringParameters"]['player_id'],
                'player_name': event["queryStringParameters"]['player_name'],
                'exp': event["queryStringParameters"]['exp'],
                'lvl': event["queryStringParameters"]['lvl'],
            }
        )