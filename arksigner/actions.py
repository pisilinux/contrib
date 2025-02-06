#!/usr/bin/python
# -*- coding: utf-8 -*-
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = ""
# NoStrip = "/"

def setup():
    shelltools.system("ar xf arksigner-pub-2.3.11.deb")
    shelltools.system("tar xvf %s/data.tar.xz --exclude=./usr/bin/arksigner/libs/libQt5*" %get.workDIR())

def build():
    pass

def install():
    pisitools.dodir("/etc/init.d")
    pisitools.insinto("/etc/init.d/", "etc/init.d/arksignerd")
    pisitools.dodir("/usr/bin/arksigner")
    pisitools.insinto("/usr/bin/arksigner", "usr/bin/arksigner/*")
