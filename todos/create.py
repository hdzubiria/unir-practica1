import json
import logging
import os
import uuid
from todos import todoTable


# Crear una nueva Nota - PARA ENTREGAR
def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    # Call todoTable
    todo_repository = todoTable.todoTable(os.environ['DYNAMODB_TABLE'])
    id = str(uuid.uuid1())
    item = todo_repository.put_todo(data['text'],id)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
