#!/bin/bash

username="alicengizkurt@gmail.com"
password="Alim**3694"
echo
evolution -u $username:$password --silent "https://mail.google.com/mail/feed/atom" |  grep -oPm1 "(?<=<title>)[^<]+" | sed '1d'
