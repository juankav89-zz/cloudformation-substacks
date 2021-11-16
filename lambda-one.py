
def lambda_handler(event, context, params=dict()):
    return {
        "statusCode": 200,
        "body": 'Hello im first lambda!'
    }