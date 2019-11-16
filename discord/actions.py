#!/usr/bin/python
# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/Discord/", "Discord/*")
    pisitools.dosym("/opt/Discord/Discord", "/usr/bin/Discord")
    shelltools.chmod(get.installDIR() + "/opt/Discord/Discord")
