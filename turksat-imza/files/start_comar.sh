#!/bin/sh
mkdir /run/turksat-imza
cd /usr/share/signNativeOsService
su -c "/usr/bin/java -jar /usr/share/signNativeOsService/signNativeOsService.jar > /dev/null 2>&1" &
echo $! > /run/turksat-imza/turksat-imza.pid
