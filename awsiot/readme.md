Run deploy.sh
./deploy.sh

It will generate AWS IoT related resources.
Don't delete certs\ folder

you can run ./undeploy.sh to remove all AWS IoT related resources.

Setup Python virtual environment and install dependences
./python_setup.sh

Run the shadow.py with proper parameter.
. venv/bin/activate
./run_shadow.sh

Search "TODO: call web core according to the value."

source https://github.com/aws/aws-iot-device-sdk-python-v2/tree/main/samples

To update_shadow call but you have to set 
. venv/bin/activate
python3 update_shadow.py

