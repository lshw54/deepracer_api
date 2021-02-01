sudo yum install jq -y

mkdir certs

key=$(aws iot create-keys-and-certificate \
    --set-as-active \
    --certificate-pem-outfile "certs/device.pem.crt" \
    --public-key-outfile "certs/public.pem.key" \
    --private-key-outfile "certs/private.pem.key")

certificateArn=$(echo $key | jq -r ".certificateArn" )
certificateId=$(echo $key | jq -r ".certificateId" )
echo $certificateArn > "certs/certificateArn.txt"
echo $certificateId > "certs/certificateId.txt"

aws cloudformation create-stack --stack-name awsiotdeepracer --template-body file://cfn.yaml \
--parameters    ParameterKey=certificateArn,ParameterValue=$certificateArn