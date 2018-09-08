#!/usr/bin/python


from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf scrivener-%s-amd64.deb" % Version)
    shelltools.system("tar xf data.tar.gz")
    shelltools.system("mkdir usr/share/icons/hicolor")
    pisitools.move("usr/share/icons/*x*", "usr/share/icons/hicolor/")

def install():
    pisitools.insinto("/", "usr")
    pisitools.removeDir("/usr/share/doc")
