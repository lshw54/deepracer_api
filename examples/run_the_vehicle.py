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
# Create the API client

client = deepracer_vehicle_api.Client(cfg['password'], cfg['ip'])
client.set_manual_mode()

# ####################################################################
# start the car
client.start_car()

#client.move_backward(timeout=3)
client.move_forward(timeout=1.7)
client.turn_right(timeout=1.0)
client.move_forward(timeout=2)
#client.turn_right(timeout=1)

# ####################################################################
# stop the car
client.stop_car()