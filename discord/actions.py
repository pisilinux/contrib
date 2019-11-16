#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    pisitools.insinto("usr/share", "Discord")
    
    shelltools.chmod(get.installDIR() + "/usr/share/Discord/Discord")
    pisitools.dosym("/usr/share/Discord/Discord", "/usr/bin/discord")
