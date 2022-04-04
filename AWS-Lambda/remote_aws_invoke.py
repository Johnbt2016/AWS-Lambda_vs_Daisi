import boto3
import json
import time

#Need to set up Github actions to sync the code with AWS Lambda

t = time.time()
client = boto3.client('lambda', region_name='us-east-1')

#No user friendly call to the remote function
response = client.invoke(FunctionName='Hello_World')

#Response is sent as a binary stream
#We need to deserialize the returned data, assuming its type

a = json.loads(response['Payload'].read().decode("utf-8"))

print(a['body'])

print(time.time() - t)
