import os
from todos import todoTable


# Borra  una nueva Nota - PARA ENTREGAR
def delete(event, context):

    # Call todoTable
    todo_repository = todoTable.todoTable(os.environ['DYNAMODB_TABLE'])
    todo_repository.delete_todo(event['pathParameters']['id'])

    # create a response
    response = {
        "statusCode": 200
    }

    return response
