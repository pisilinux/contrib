#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("mkdir -p /usr/lib64/")
    os.system("ln -s /usr/lib/x86_64-linux-gnu/libpcsclite.so /usr/lib64/")
    os.system("ln -s /usr/lib/x86_64-linux-gnu/libpcsclite.so.1 /usr/lib64/")
    os.system("ln -s /usr/lib/x86_64-linux-gnu/libpcsclite.so.1.0.0 /usr/lib64/")
