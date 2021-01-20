import os 
import yaml
import time
import deepracer_vehicle_api

# ####################################################################
# Load the configuration
#
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path,"config.yml"), 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# ####################################################################
# Create the API client and login

client = deepracer_vehicle_api.Client(cfg['password'], cfg['ip'])

# ####################################################################
# 
print(client.set_calibration_mode())

print(client.set_calibration_throttle(cfg["calibration"]["throttle"]))
print(client.set_calibration_angle(cfg["calibration"]["angle"]))

print("Throttle", client.get_calibration_throttle())
print("Angle", client.get_calibration_angle())
