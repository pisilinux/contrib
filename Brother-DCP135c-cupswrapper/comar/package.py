#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/usr/local/Brother/cupswrapper/cupswrapperDCP135c-1.0.1"):
        os.system("/usr/local/Brother/cupswrapper/cupswrapperDCP135c-1.0.1 -i")

def preRemove():
    if os.path.exists("/usr/local/Brother/cupswrapper/cupswrapperDCP135c-1.0.1"):
        os.system("/usr/local/Brother/cupswrapper/cupswrapperDCP135c-1.0.1 -e")
