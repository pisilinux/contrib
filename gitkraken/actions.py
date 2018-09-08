#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf gitkraken-amd64.deb")
    shelltools.system("tar xvf data.tar.xz --exclude=usr/bin")
    shelltools.system("sed -i 's Icon=app Icon=gitkraken ' usr/share/applications/gitkraken.desktop")
    shelltools.system("mv usr/share/pixmaps/app.png usr/share/pixmaps/gitkraken.png")
def install():
    pisitools.insinto("/", "usr")   
    pisitools.dosym("/usr/share/gitkraken/gitkraken", "/usr/bin/gitkraken")   

