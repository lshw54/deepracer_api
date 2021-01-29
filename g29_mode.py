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
try:
    while True:
        events = pygame.event.get()
        throttle_Speed = -0.1
        for event in events:
            if event.type == pygame.JOYAXISMOTION and event.axis == 0: #stering_angle
                if event.value < -1:
                     event.value = -1
                else: 
                    client.move(steering_angle=event.value, throttle=throttle_Speed, max_speed=1.0)
            elif event.type == pygame.JOYAXISMOTION and event.axis == 2: # throttle
                client.start_car()
                client.move(steering_angle=0.00, throttle= throttle_Speed, max_speed=1.0)
            elif event.type == pygame.JOYAXISMOTION and event.axis == 3: # stop the car break 
                client.stop_car()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
                print("O")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4: # + speed
                throttle_Speed += -0.15
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 5: # - speed
                throttle_Speed = throttle_Speed + -0.15
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 12:
                throttle_Speed == -0.15
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 14:
                throttle_Speed == -1.0
                

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
