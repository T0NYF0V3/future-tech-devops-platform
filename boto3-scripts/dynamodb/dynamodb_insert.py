import boto3
from datetime import datetime

# Create DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1'
)

# Reference table
table = dynamodb.Table('DevOpsUsers')

# Insert item
response = table.put_item(
    Item={
        'user_id': 'dev001',
        'name': 'Gustavo',
        'role': 'DevOps Engineer',
        'project': 'Future Tech DevOps Platform',
        'created_at': datetime.now().isoformat()
    }
)

print("\n=== INSERT OPERATION SUCCESSFUL ===")
print(response)
