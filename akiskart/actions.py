#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    shelltools.system("ar xf akis_1.6_amd64.deb")
    shelltools.system("tar xvf %s/data.tar.gz --exclude=usr/share/gnome-control-center --exclude=usr/bin " %get.workDIR())

def build():
    pass

def install():
    pisitools.dolib("usr/lib/*")
    pisitools.insinto("/usr/share/akis", "usr/share/akis/akia.jar")