import boto3
import json

client = boto3.client('lambda', region_name='us-east-1')

test_event = dict()

response = client.invoke(
  FunctionName='Hello_World',
  Payload=json.dumps(test_event),
)

a = json.loads(response['Payload'].read().decode("utf-8"))

print(a['body'])

