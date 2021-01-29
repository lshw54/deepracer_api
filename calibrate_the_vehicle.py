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

# ####################################################################
#

client.start_car()
client.move(steering_angle=0.05, throttle=0.80, max_speed=1.0)
client.move(steering_angle=0.05, throttle=0.80, max_speed=1.0)
client.move(steering_angle=0.05, throttle=0.54, max_speed=1.0)
client.move(steering_angle=0.05, throttle=0.54, max_speed=1.0)
client.move(steering_angle=0.05, throttle=0.54, max_speed=1.0)

