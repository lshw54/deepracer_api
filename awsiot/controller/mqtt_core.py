import sys
import json
import boto3
from logger import Logger
from ratelimit import limits

logger = Logger(logger="Deepracer-Api").getlog()


class DeepracerVehicleApiError(Exception):
    pass


class Client:
    def __init__(self, thingName, region_name, password="", ip="127.0.0.1", name="deep_racer"):
        # logger.info("Create client with ip = %s", ip)
        self.password = password
        self.name = name
        self.ip = ip
        self.headers = None

        # basic path form deepracer console
        self.URL = "https://" + self.ip + "/"

        self.manual = True
        self.start = False
        self.thingName = thingName
        self.client = boto3.client('iot-data', region_name=region_name)

    # General purpose methods

    def get_is_usb_connected(self):
        return self._get("api/is_usb_connected")

    def get_battery_level(self):
        return self._get("api/get_battery_level")

    #  methods for running autonomous mode

    def set_autonomous_mode(self):
        # Set the car to use the autonomous mode and not care about input from this program
        self.stop_car()
        data = {"drive_mode": "auto"}
        return self._put("api/drive_mode", data)

    def set_throttle_percent(self, throttle_percent):
        # Set the percent throttle from 0-100% (note for manual mode this has no effect)
        data = {"throttle": throttle_percent}
        return self._put("api/max_nav_throttle", data)

    #  methods for running manual mode

    def set_manual_mode(self):
        # Set the car to take in input from manual channels (ie this program)
        self.stop_car()
        data = {"drive_mode": "manual"}
        return self._put("api/drive_mode", data)

    def start_car(self):
        data = {"start_stop": "start"}
        return self._put("api/start_stop", data)

    def stop_car(self):
        data = {"start_stop": "stop"}
        return self._put("api/start_stop", data)

    def move(self, steering_angle, throttle, max_speed):
        # Set angle and throttle commands from -1 to 1
        data = {"angle": steering_angle,
                "throttle": throttle, "max_speed": max_speed}
        return self._put("api/manual_drive", data)

    # models

    def get_models(self):
        return self._get("api/models")

    def get_uploaded_models(self):
        return self._get("api/uploaded_model_list")

    # calibration

    def set_calibration_mode(self):
        return self._get("api/set_calibration_mode")

    def get_calibration_angle(self):
        return self._get("api/get_calibration/angle")

    def get_calibration_throttle(self):
        return self._get("api/get_calibration/throttle")

    def set_calibration_throttle(self, throttle):
        return self._put("api/set_calibration/throttle", throttle)

    def set_calibration_angle(self, angel):
        return self._put("api/set_calibration/angle", angel)

    # helper methods

    def _get(self, url, check_status_code=True):
        logger.debug("> Get %s", url)
        return self._mqtt("put", url, {}, check_success=True)

    def _put(self, url, data, check_success=True):
        logger.debug("> Put %s with %s", url, data)
        return self._mqtt("put", url, data, check_success=True)

    # rate limited to 20 call per second
    @limits(calls=20, period=1, raise_on_limit=False)
    def _mqtt(self, method, url, data, check_success=True):
        payload = json.dumps({
            'state': {
                'desired': {
                    'apiCall': {
                        'method': method,
                        'url': url,
                        'data': data
                    }
                }
            }
        })

        print("Call _mqtt")
        response = self.client.update_thing_shadow(
            thingName=self.thingName,
            payload=payload
        )

        return response['payload'].read()
