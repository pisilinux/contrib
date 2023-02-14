#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    shelltools.system("unzip Akia_linux_6_4_1_deb.zip")
    shelltools.system("ar xf Akia_linux_6_4_1.deb")
    shelltools.system("tar xvf %s/data.tar.gz --exclude=usr/share/gnome-control-center --exclude=usr/bin " %get.workDIR())

def build():
    pass

def install():
    pisitools.insinto("/usr/share/akia", "opt/Akia/akia.jar")
