region=ap-east-1

sudo yum install jq -y

mkdir -p deepracer/certs

key=$(aws iot create-keys-and-certificate \
    --region $region \
    --set-as-active \
    --certificate-pem-outfile "deepracer/certs/device.pem.crt" \
    --public-key-outfile "deepracer/certs/public.pem.key" \
    --private-key-outfile "deepracer/certs/private.pem.key")

certificateArn=$(echo $key | jq -r ".certificateArn" )
certificateId=$(echo $key | jq -r ".certificateId" )
echo $certificateArn > "deepracer/certs/certificateArn.txt"
echo $certificateId > "deepracer/certs/certificateId.txt"

aws cloudformation create-stack --stack-name awsiotdeepracer \
--region $region \
--template-body file://cfn.yaml \
--parameters    ParameterKey=certificateArn,ParameterValue=$certificateArn