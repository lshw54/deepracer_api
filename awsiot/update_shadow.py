import boto3

client = boto3.client('iot-data')

response = client.get_thing_shadow(
    thingName='awsiotdeepracer-AWSDeepRacerThing-1RBJZUBPFCEFD'
)

print(response)
print(response.payload)

response = client.update_thing_shadow(
    thingName='awsiotdeepracer-AWSDeepRacerThing-1RBJZUBPFCEFD',
    payload=response.payload 
)

print(response)