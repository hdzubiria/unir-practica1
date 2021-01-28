import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def translate(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # Traduccion
    target_lang = event['pathParameters']['language']
    text_to_translate = result['Item']['text']

    translating = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    translated = translating.translate_text(Text=text_to_translate, SourceLanguageCode='en', TargetLanguageCode=target_lang)
    
    result['Item']['text'] = translated['TranslatedText']

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response