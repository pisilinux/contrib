#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    pisitools.insinto("usr/share", "discord")
    pisitools.dosym("/usr/share/discord/Discord", "/usr/bin/discord")