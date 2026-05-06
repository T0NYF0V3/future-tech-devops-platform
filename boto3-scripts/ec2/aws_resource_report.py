import boto3

# Create AWS clients
ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

print("\n========== AWS RESOURCE REPORT ==========\n")

# =========================
# EC2 INSTANCES
# =========================
print("EC2 INSTANCES:\n")

ec2_response = ec2.describe_instances()

for reservation in ec2_response['Reservations']:
    for instance in reservation['Instances']:

        print(f"- ID: {instance['InstanceId']}")
        print(f"  State: {instance['State']['Name']}")
        print(f"  Type: {instance['InstanceType']}")
        print()

# =========================
# S3 BUCKETS
# =========================
print("\nS3 BUCKETS:\n")

s3_response = s3.list_buckets()

for bucket in s3_response['Buckets']:
    print(f"- {bucket['Name']}")

# =========================
# DYNAMODB TABLES
# =========================
print("\nDYNAMODB TABLES:\n")

ddb_response = dynamodb.list_tables()

for table in ddb_response['TableNames']:
    print(f"- {table}")

print("\n=========================================\n")
