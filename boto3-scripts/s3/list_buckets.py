import boto3

# Create S3 client
s3 = boto3.client('s3')

# Retrieve bucket list
response = s3.list_buckets()

print("\n========== S3 BUCKETS ==========\n")

for bucket in response['Buckets']:
    print(f"Bucket Name: {bucket['Name']}")

print("\n================================\n")
