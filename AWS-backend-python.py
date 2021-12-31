import json 
import boto3

# Create a handle object for dynamo db database
db = boto3.resource('dynamodb')
# Create a handle object for the Colors table
table = db.Table('Colors')

# Handler function
def lambda_handler(event, context):
    # Get an item with ID = 01 in the table
    response = table.get_item(Key = {'ID': "01"})
    # Return the value of the Color with that id
    return response['Item']['Color']