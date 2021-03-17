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

get_os = platform.system()

pygame.init()
joystick_count = pygame.joystick.get_count()
for i in range(joystick_count):
    j = pygame.joystick.Joystick(i)
    j.init()


def event_loop():
    global done, drive, steer
    logger.info(u"Running On %s", get_os)
    while not done:
        pygame.init()
        events = pygame.event.get()
        for event in events:
            if get_os == "Linux":
                if event.type == pygame.JOYAXISMOTION and event.axis == 0:  # stering_angle
                    if event.value < 0.2 and event.value > -0.2:  # turn right
                        steer = 0
                    elif event.value < -1:  # turn left
                        event.value = -1
                    else:
                        steer = event.value
                elif event.type == pygame.JOYAXISMOTION and event.axis == 4:  # Throttle
                    if event.value < 0.035 and event.value > -0.1:
                        drive = 0
                    elif event.value < -1:
                        event.value = -1
                    elif (event.value >= -1 and event.value < -0.1) or (
                        event.value <= 1 and event.value > 0.035
                    ):
                        drive = event.value * -1
                elif event.type == pygame.JOYBUTTONDOWN and event.button == 0:  # parking
                    drive = 0
            elif get_os == "Windows":
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
            elif get_os == "Darwin":
                if event.type == pygame.JOYAXISMOTION and event.axis == 0:  # stering_angle
                    if event.value < 0.2 and event.value > -0.2: # turn right
                        steer = 0
                    elif event.value < -1 : # turn left
                        event.value = -1
                    else:
                        steer = event.value
                elif event.type == pygame.JOYAXISMOTION and event.axis == 5: # Throttle
                    if event.value < 0.035 and event.value > -0.1: 
                        drive = 0
                    elif event.value < -1 :
                        event.value = -1 
                    elif (event.value >= -1 and event.value < -0.1) or (event.value <= 1 and event.value > 0.035):
                        drive = event.value * -1
                elif event.type == pygame.JOYBUTTONDOWN and event.button == 1: # parking
                    drive = 0


def main():
    client = Client(password=os.getenv("password"), ip=os.getenv("hostIp"))
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
