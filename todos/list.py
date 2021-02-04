import json
import os
from todos import decimalencoder
from todos import todoTable


def list(event, context):
    
    # Call todoTable
    todo_repository = todoTable.todoTable(os.environ['DYNAMODB_TABLE'])
    items = todo_repository.scan_todo()
    
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(items['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
