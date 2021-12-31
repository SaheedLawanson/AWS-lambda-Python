import json 
import boto3

db = boto3.resource('dynamodb')
table = db.Table('Colors')

def lambda_handler(event, context):
    response = table.get_item(Key = {'ID': "01"})
    return response['Item']['Color']