#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/local", "./local/*")
    pisitools.insinto("/usr/lib/", "./lib64/libbrscandec3.so.1.0.0")    
    pisitools.insinto("/usr/lib/", "./lib64/sane/libsane-brother3.so.1.0.7")
    pisitools.insinto("/usr/lib/sane/", "./lib64/libbrscandec3.so.1.0.0")    
    pisitools.insinto("/usr/lib/sane/", "./lib64/sane/libsane-brother3.so.1.0.7")
    pisitools.insinto("/usr/bin/", "./local/Brother/sane/brsaneconfig3*")   
