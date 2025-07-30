def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }

# For local testing
if __name__ == '__main__':
    response = lambda_handler({}, None)
    print(response)