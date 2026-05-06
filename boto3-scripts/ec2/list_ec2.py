import boto3

# Create EC2 client
ec2 = boto3.client(
    'ec2',
    region_name='us-east-1'
)

# Retrieve EC2 instances
response = ec2.describe_instances()

print("\n========== EC2 INSTANCES ==========\n")

for reservation in response['Reservations']:
    for instance in reservation['Instances']:

        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        instance_type = instance['InstanceType']

        print(f"Instance ID   : {instance_id}")
        print(f"State         : {state}")
        print(f"Instance Type : {instance_type}")
        print("-" * 40)

print("\n===================================\n")
