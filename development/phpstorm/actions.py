#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/phpstorm", "PhpStorm-212.5457.49/*")
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
