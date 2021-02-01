certificateId=$(cat "certs/certificateId.txt")
echo $certificateId

aws iot update-certificate \
    --certificate-id $certificateId \
    --new-status INACTIVE

aws iot delete-certificate \
    --certificate-id $certificateId
    
aws cloudformation delete-stack --stack-name awsiotdeepracer