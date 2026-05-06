import json
import random

def lambda_handler(event, context):

    responses = [
        "DevOps pipeline active",
        "Infrastructure deployed",
        "Lambda execution successful",
        "Monitoring enabled"
    ]

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': random.choice(responses)
        })
    }
