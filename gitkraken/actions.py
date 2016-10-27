#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "."

def install():   
    pisitools.insinto("/usr/share/", "gitkraken")        
    pisitools.insinto("/usr/bin/", "./gitkraken/gitkraken")   
    pisitools.insinto("/usr/share/doc/", "./gitkraken/LICENSE")    
