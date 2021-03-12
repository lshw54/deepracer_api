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
max_speed = 0.25
done = False

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

get_os = platform.system()

def event_loop():
    global done, drive, steer
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION and event.axis == 0:  # stering_angle
                if event.value < -1:
                    event.value = -1
                else:
                    steer = event.value
                    drive = drive
                    max_speed = max_speed
            elif event.type == pygame.JOYAXISMOTION and event.axis == 1 and get_os == "Windows":
                drive = event.value
            elif event.type == pygame.JOYAXISMOTION and event.axis == 2 and get_os == "Darwin":
                drive = event.value
            elif event.type == pygame.JOYAXISMOTION and event.button == 12:  # D1 throttle
                max_speed = 0.25
            elif event.type == pygame.JOYAXISMOTION and event.button == 13:  # D2 throttle
                max_speed = 0.30
            elif event.type == pygame.JOYAXISMOTION and event.button == 14:  # D3 throttle
                max_speed = 0.45
            elif event.type == pygame.JOYAXISMOTION and event.button == 15:  # D4 throttle
                max_speed = 0.60
            elif event.type == pygame.JOYAXISMOTION and event.button == 16:  # D5 throttle
                max_speed = 0.75
            elif event.type == pygame.JOYAXISMOTION and event.button == 17:  # D6 throttle
                max_speed = 1.0
            elif event.type == pygame.JOYAXISMOTION and event.axis == 2 and get_os == "Windows": # Parking
                done = True
            elif event.type == pygame.JOYAXISMOTION and event.axis == 3 and get_os == "Darwin":  # Parking
                done = True
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:  # Rear
                max_speed = -1.0
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 5:  # Drive
                max_speed = 1.0


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
