import os
import time
import yaml
import threading
import inputs  # https://inputs.readthedocs.io/en/latest/user/intro.html

import deepracer_vehicle_api

steer = 0
drive = 0
done = False
stop = False

def event_loop():
    """
    This function is called in a loop, and will get the events from the
    controller and send them to the functions we specify in the `event_lut`
    dictionary
    """
    global done, drive, steer, stop
    steer2 = steer3 = 0
    while not done:
        events = inputs.get_gamepad()
        for event in events:
            if event.code == "ABS_Z":
                drive = event.state / 256.0
            if event.code == "ABS_RZ":
                drive = event.state / -256.0 
            
            if event.code == "ABS_X":
                steer = event.state / 256.0 / 128.0
            
            if event.code == "BTN_NORTH":
                done = True
            elif event.code.find("BTN_") == 0:
                stop = True


def main():
    """Process all events forever."""
    
    # ####################################################################
    # Load the configuration
    #
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(dir_path,"config.yml"), 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    # ####################################################################
    # Create the API client

    client = deepracer_vehicle_api.Client(cfg['password'], cfg['ip'])
    client.set_manual_mode()
    client.start_car()
    t1 = threading.Thread(target=event_loop, name='t1')
    t1.start()
    max_speed = -0.75
    global done, drive, steer, stop
    while not done:
        if drive < 0 and drive < max_speed:
            drive = max_speed
        elif drive > max_speed * -1:
            drive = max_speed * -1
        client.move(steer, drive)
        print("Steering command: " + str(steer) + " Throttle command: " + str(drive))
        last_drive = drive
        last_steer = steer
        # time.sleep(0.1)

        if stop:
            client.stop_car()
            print("Emergency stop")
            time.sleep(2)
            print("Start the car")
            client.start_car()
            stop = False

    client.stop_car()
    t1.join()


if __name__ == "__main__":
    main()
