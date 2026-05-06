import boto3

# Create DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1'
)

# Reference table
table = dynamodb.Table('DevOpsUsers')

# Read item
response = table.get_item(
    Key={
        'user_id': 'dev001'
    }
)

item = response.get('Item')

print("\n=== RETRIEVED ITEM ===\n")

if item:
    for key, value in item.items():
        print(f"{key}: {value}")
else:
    print("Item not found.")
