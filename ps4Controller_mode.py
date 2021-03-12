import os
import platform
import yaml
import time
import threading
import argparse
import pygame

from awsdeepracer_control import Client
from core.logger import Logger

logger = Logger(logger="Gamepad_mode").getlog()

steer = 0
drive = 0
max_speed = 1
done = False

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

def event_loop():
    global done, drive, steer
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION and event.axis == 0:  # stering_angle
                if event.value < 0.2 and event.value > -0.2: # turn right
                    steer = 0
                elif event.value < -1 : # turn left
                    event.value = -1
                else:
                    steer = event.value
            elif event.type == pygame.JOYAXISMOTION and event.axis == 3: # Throttle
                if event.value < 0.035 and event.value > -0.1: 
                    drive = 0
                elif event.value < -1 :
                    event.value = -1 
                elif (event.value >= -1 and event.value < -0.1) or (event.value <= 1 and event.value > 0.035):
                    drive = event.value * -1
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 0: # parking
                drive = 0


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, "config.yml"), "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    logger.info("Create client with ip = %s", cfg["ip"])
    logger.info("Login to %s with password %s", cfg["ip"], cfg["password"])
    client = Client(cfg["password"], cfg["ip"])
    client.set_manual_mode()
    logger.info("Set the Deepracer to manual mode.")
    client.start_car()
    t1 = threading.Thread(target=event_loop, name="t1")
    t1.start()
    global done, drive, steer
    while not done:
        client.move(steer, drive, max_speed)
        print(
            "Steering command: "
            + str(steer)
            + " Throttle command: "
            + str(drive)
            + " Max_speed: "
            + str(max_speed)
        )
    client.stop_car()
    t1.join

if __name__ == "__main__":
    main()
