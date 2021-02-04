import os
import json
from todos import decimalencoder
from todos import todoTable


def get(event, context):
    
    # Call todoTable
    todo_repository = todoTable.todoTable(os.environ['DYNAMODB_TABLE'])
    id= event['pathParameters']['id']
    item = todo_repository.get_todo(id)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
