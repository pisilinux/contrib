#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/local/brother/scanner/brscan4", "./opt/brother/scanner/brscan4/*")    
    pisitools.insinto("/usr/lib/sane/libsane-brother4.so.1", "./usr/lib64/sane/libsane-brother4.so.1.0.7")       
    pisitools.insinto("/usr/bin/", "./opt/brother/scanner/brscan4/brsaneconfig4")  
