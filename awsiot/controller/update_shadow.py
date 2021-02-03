
import boto3
import json
import time

import random
from random import choices
from mqtt_core import Client
import string
fake = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


region = 'ap-east-1'
thingName = 'awsiotdeepracer-AWSDeepRacerThing-L19K9MPMDSIL'

# client = boto3.client('iot-data', region_name=region)
# response = client.get_thing_shadow(
#     thingName=thingName
# )
# print(response)
# t = json.loads(response['payload'].read())
# print(t)
for i in range(100):
    mqtt_client = Client(thingName, region)
    if i % 2 == 0:
        t = mqtt_client.start_car()
    else:
        t = mqtt_client.stop_car()
    print(t)

    # payload = json.dumps({
    #     'state': {
    #         'desired': {
    #             'apiCall': {
    #                 'method': choices(['post', 'get']),
    #                 'url': choices(['api/start_stop', 'api/drive_mode']),
    #                 'data': {"start_stop": choices(['stop', 'start'])}
    #             }
    #         }
    #     }
    # })
    # response = client.update_thing_shadow(
    #     thingName='awsiotdeepracer-AWSDeepRacerThing-1RBJZUBPFCEFD',
    #     payload=payload
    # )
    # # print(response)
    # t = response['payload'].read()
