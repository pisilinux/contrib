#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    shelltools.system("rpm2targz dcp135clpr-1.0.1-1.i386.rpm")
    shelltools.system("tar -zxvf dcp135clpr-1.0.1-1.i386.tar.gz")
    pisitools.insinto("/", "usr")
    shelltools.system("rm -rf *")
