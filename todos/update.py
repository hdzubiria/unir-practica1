import json
import logging
import os

from todos import decimalencoder
from todos import todoTable


def update(event, context):
    data = json.loads(event['body'])
    if 'text' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")

    # Call todoTable
    todo_repository = todoTable.todoTable(os.environ['DYNAMODB_TABLE'])
    item = todo_repository.update_todo(data['text'],
                                            event['pathParameters']['id'],
                                            data['checked']
                                        )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
