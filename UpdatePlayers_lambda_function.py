import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('A3_Players')
    
    if event["queryStringParameters"]['player_id'] and event["queryStringParameters"]['exp'] and event["queryStringParameters"]['lvl']:
        table.update_item(
            Key={
                'player_id': event["queryStringParameters"]['player_id'],
            },
            UpdateExpression='SET exp = :e, lvl = :l',
            ExpressionAttributeValues={
                ':e': event["queryStringParameters"]['exp'],
                ':l': event["queryStringParameters"]['lvl']
            }
        )
    
    response = table.get_item(
        Key={
            'player_id': event["queryStringParameters"]['player_id']
            }
    )
   
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }