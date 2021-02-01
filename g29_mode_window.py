import pygame
import os
import yaml
import time
from core.web_core import Client

# ####################################################################
# Load the configuration
#
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "config.yaml"), "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# ####################################################################
# Create the API client and login

client = Client(cfg["password"], cfg["ip"])
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
steer = 0
mspeed = 0.25
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION and event.axis == 0: #stering_angle
                if event.value < -1:
                     event.value = -1
                else:
                    client.move(steering_angle=event.value, throttle= -1.0, max_speed=mspeed)
                    steer = event.value
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
                mspeed = 0.25
                print(mspeed)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 13:
                mspeed = 0.30
                print(mspeed)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 14:
                mspeed = 0.45
                print(mspeed)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 15:
                mspeed = 0.60
                print(mspeed)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 16:
                mspeed = 0.75
                print(mspeed)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 17:
                mspeed = 1.0
                print(mspeed)
            elif event.type == pygame.JOYAXISMOTION and event.axis == 1 and event.value > -1:
                client.start_car()
                client.move(steering_angle=steer, throttle= -1.0, max_speed=mspeed)
                print(steer)
                print(mspeed)

            elif event.type == pygame.JOYAXISMOTION and event.axis == 2: # stop the car break 
                client.stop_car()
                mspeed = 0.0
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
                print("O")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4: # + speed
                print("123")#throttle_Speed += -0.15
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 5: # - speed
                print("123")#throttle_Speed = throttle_Speed + -0.15
                
                #client.move(steering_angle=0.00, throttle= throttle_Speed, max_speed=1.0)
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
