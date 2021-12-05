#!/usr/bin/python
# Created For PisiLinux
from pisi.actionsapi import pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/discord/", "Discord/*")
    pisitools.dosym('/opt/discord/Discord', '/usr/bin/discord')