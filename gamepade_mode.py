import os
import yaml
import time
import threading
import argparse
from inputs import get_gamepad
from core.web_core import Client
from core.logger import Logger

logger = Logger(logger="Gamepad_mode").getlog()

steer = 0
drive = 0
max_speed = 1
done = False


def event_loop():
    global done, drive, steer
    while not done:
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_RZ":
                drive = event.state / -256.0
            # print('\t', event.ev_type, event.code, event.state)
            if event.code == "ABS_X":
                steer = (event.state - 128) / 128.0
            if event.code == "ABS_RZ":
                drive = event.state / -256.0
            elif event.code == "ABS_Z":
                drive = event.state / 256.0
            if event.code == "BTN_NORTH":
                done = True


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path, "config.yaml"), "r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
    logger.info("Create client with ip = %s", cfg["ip"])
    logger.info("Login to %s with password %s", cfg["ip"], cfg["password"])
    client = Client(cfg["password"], cfg["ip"])
    client.set_manual_mode()
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
