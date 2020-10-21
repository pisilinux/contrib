#!/usr/bin/python

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
NoStrip = ["/"]




def install():
    pisitools.insinto("/usr/share/", "gradle-4.1/")
    pisitools.dosym("/usr/share/gradle-4.1/bin/gradle", "/usr/bin/gradle")