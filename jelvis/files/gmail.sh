#!/bin/bash

username=""
password=""
echo
google-chrome-stable -u $username:$password --silent "https://mail.google.com" |  grep -oPm1 "(?<=<title>)[^<]+" | sed '1d'
