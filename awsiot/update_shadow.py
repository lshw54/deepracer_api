import boto3
import json
import time

import random
from random import choices
from mqtt_core import Client
import string
fake = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

client = boto3.client('iot-data', region_name='us-east-1')

response = client.get_thing_shadow(
    thingName='awsiotdeepracer-AWSDeepRacerThing-1RBJZUBPFCEFD'
)

# print(response)
t = json.loads(response['payload'].read())
print(t)
for i in range(100):
    payload = json.dumps({
        'state': {
            'desired': {
                'apiCall': {
                    'method': choices(['post', 'get']),
                    'url': choices(['api/start_stop', 'api/drive_mode']),
                    'data': {"start_stop": choices(['stop', 'start'])}
                }
            }
        }
    })

    mqtt_client = Client(
        thingName='awsiotdeepracer-AWSDeepRacerThing-1RBJZUBPFCEFD')
    t = mqtt_client.start_car()
    # response = client.update_thing_shadow(
    #     thingName='awsiotdeepracer-AWSDeepRacerThing-1RBJZUBPFCEFD',
    #     payload=payload
    # )
    # # print(response)
    # t = response['payload'].read()
    print(t)
