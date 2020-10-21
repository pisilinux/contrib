#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("echo '0.0.0.0 get.code-industry.net' >> /etc/hosts")