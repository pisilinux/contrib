#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/bin/", "./usr/bin/apm-beta")    
    pisitools.insinto("/usr/bin/", "./usr/bin/atom-beta")       
    pisitools.insinto("/usr/share/atom-beta/", "./usr/share/atom-beta/*")
    pisitools.insinto("/usr/share/doc/atom-beta", "./usr/share/doc/atom-beta/*")
