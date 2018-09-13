#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    shelltools.system("rpm2targz slack-3.3.1-0.1.fc21.x86_64.rpm")
    shelltools.system("tar -zxvf slack-3.3.1-0.1.fc21.x86_64.tar.gz")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "etc")