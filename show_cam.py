import os
import yaml
import time
from awsdeepracer_control import Client

from core import deepracer_cam
import cv2

client = Client(password=os.getenv('password'), ip=os.getenv('hostIp'))

cam = deepracer_cam.DeepracerCam(client)
cam.start()
time.sleep(1)
i = 0
while True:
    image = cam.get_image(timeout=1)
    if image is not None:
        cv2.imshow("Deepracer_Cam", image)
    else:
        print("waiting", i)
        i = i + 1
    if cv2.waitKey(1) == 27:
        exit(0)