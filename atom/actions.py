#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/bin/", "./usr/bin/apm")    
    pisitools.insinto("/usr/bin/", "./usr/bin/atom")       
    pisitools.insinto("/usr/share/atom/", "./usr/share/atom/*")
    pisitools.insinto("/usr/share/doc/atom", "./usr/share/doc/atom/*")
