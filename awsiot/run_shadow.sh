endpointAddress=$(aws iot describe-endpoint --endpoint-type iot:Data-ATS | jq -r ".endpointAddress")

echo $endpointAddress
AWSDeepRacerThing=$(aws cloudformation describe-stacks --stack-name awsiotdeepracer \
--query 'Stacks[0].Outputs[?OutputKey==`AWSDeepRacerThing`].OutputValue' --output text)
echo $AWSDeepRacerThing

python3 shadow.py --endpoint $endpointAddress --cert "certs/device.pem.crt" --key "certs/private.pem.key" --thing-name $AWSDeepRacerThing