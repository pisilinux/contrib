#!/usr/bin/python

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/"]

def setup():
    shelltools.system("unzip android-studio-ide-162.4069837-linux.zip")

def install():
    pisitools.insinto("/opt/android-studio", "android-studio/*")
    pisitools.dosym("/opt/android-studio/bin/studio.sh", "/usr/bin/android-studio")
