#!/bin/sh
mkdir /run/belgenet
cd /usr/share/signNativeOsService
su -c "/usr/bin/java -jar /usr/share/signNativeOsService/signNativeOsService.jar > /dev/null 2>&1" &
echo $! > /run/belgenet/belgenet.pid
