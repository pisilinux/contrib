#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    shelltools.system("rpm2targz lazarus-1.8.4-0.x86_64.rpm")
    shelltools.system("tar -zxvf lazarus-1.8.4-0.x86_64.tar.gz")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "etc")
    shelltools.export("$THEPREFIX/usr/lib64/fpc/3.0.4/samplecfg", "$THEPREFIX/usr/lib64/fpc/3.0.4/ $ETCDIR")
    shelltools.chmod("usr/lib64/lazarus/startlazarus", 0777)