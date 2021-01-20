import os
import yaml
import time
import deepracer_vehicle_api

# ####################################################################
# Load the configuration
#
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "config.yaml"), "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# ####################################################################
# Create the API client

client = deepracer_vehicle_api.Client(cfg["password"], cfg["ip"])
client.set_manual_mode()

# ####################################################################
# start the car
# client.start_car()
# client.move_forward(timeout=3)
# client.move(steering_angle=0.00, throttle=1.0, max_speed=1.0)
# client.stop_car()
client.show_vehicle_info()

print(client.get_battery_level())
