import os 
import yaml
import time
import json
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
client.show_vehicle_info()

