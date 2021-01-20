import os 
import yaml
import time
import deepracer_vehicle_api

import deepracer_cam
import cv2

# ####################################################################
# Load the configuration
#
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path,"config.yml"), 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# ####################################################################
# Create the API client

client = deepracer_vehicle_api.Client(cfg['password'], cfg['ip'])

cam = deepracer_cam.DeepracerCam(client)
cam.start()
time.sleep(1)
i=0
while True:
    image = cam.get_image(timeout=1)
    if image is not None:
        cv2.imshow('i', image)
    else:
        print("waiting", i)
        i = i + 1
    if cv2.waitKey(1) == 27:
        exit(0)
