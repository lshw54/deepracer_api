Run deploy.sh
./deploy.sh

It will generate AWS IoT related resources.
Don't delete deepracer\certs\ folder

you can run ./undeploy.sh to remove all AWS IoT related resources.

There are 2 projects: controller and deepracer.

Go to controller folder.
Setup Python virtual environment and install dependences
./setup.sh
To update_shadow call but you have to use virtual environment
open update_shadow.py and change the thingName.
. venv/bin/activate
python3 update_shadow.py

Run the shadow.py with proper parameter.
. venv/bin/activate
./run_shadow.sh

source https://github.com/aws/aws-iot-device-sdk-python-v2/tree/main/samples



