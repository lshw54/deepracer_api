endpointAddress=$(aws iot describe-endpoint --endpoint-type iot:Data-ATS --region us-east-1  | jq -r ".endpointAddress")

echo $endpointAddress
AWSDeepRacerThing=$(aws cloudformation describe-stacks --stack-name awsiotdeepracer --region us-east-1 \
--query 'Stacks[0].Outputs[?OutputKey==`AWSDeepRacerThing`].OutputValue' --output text)
echo $AWSDeepRacerThing

python3 shadow.py --endpoint $endpointAddress --cert "certs/device.pem.crt" --key "certs/private.pem.key" --thing-name $AWSDeepRacerThing