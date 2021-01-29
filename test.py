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
        for event in events:
            if event.type == pygame.JOYAXISMOTION and event.axis == 0 and event.value < 0:
                client.move(steering_angle=-1.0, throttle=-0.20, max_speed=1.0)
            elif event.type == pygame.JOYAXISMOTION and event.axis == 0 and event.value > 0:
                client.move(steering_angle=1.0, throttle=-0.20, max_speed=1.0)
            elif event.type == pygame.JOYAXISMOTION and event.axis == 2:
                client.start_car()
                client.move(steering_angle=0.00, throttle=-0.20, max_speed=1.0)
            elif event.type == pygame.JOYAXISMOTION and event.axis == 3:
                client.stop_car()
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 2:
                print("O")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                print("+")
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 5:
                print("-")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()