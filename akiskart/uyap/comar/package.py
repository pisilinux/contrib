#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    libs=["libpcsclite.so","libpcsclite.so.1", "libpcsclite.so.1.0.0"]
    os.system("mkdir -p /usr/lib64/")
    for i in libs:
        os.system("ln -s /usr/lib/%s /usr/lib64/" % i)
