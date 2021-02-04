import os
import json
from todos import todoTable
from todos import decimalencoder

def translate(event, context):

    # Call todoTable
    todo_repository = todoTable.todoTable(os.environ['DYNAMODB_TABLE'])
    id= event['pathParameters']['id']
    target_lang = event['pathParameters']['language']

    item = todo_repository.translate_todo(id,target_lang)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response