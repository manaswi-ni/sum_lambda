def lambda_handler(event=None, context=None):
    # Default values
    a = 5
    b = 7
    total = a + b

    return {
        'statusCode': 200,
        'body': f'Sum of {a} and {b} is {total}'
    }
