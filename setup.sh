#!/bin/bash
# define hostIp and password for deepracer
if [ -e "hostname_password" ]; then
    echo "host set"
else
    read -p "hostIp: " hostIp
    read -p "password: " password

    echo $hostIp > ./hostname_password
    echo $password >> ./hostname_password

    hostIp=""
    password=""
fi

index=0

while read line
do
if [ "$index" -eq "0" ]; then
    hostIp=$line
    index=1
else
    password=$line
fi
done < ./hostname_password

echo "hostIp is $hostIp"
echo "password is $password"

export hostIp=$hostIp
export password=$password

xhost +