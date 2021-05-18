#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/usr"]
IgnoreAutodep = True


def install():
    pisitools.insinto("/usr/share/netbeans", "./*")
    pisitools.dosym("/usr/share/netbeans/bin/netbeans", "/usr/bin/netbeans") 
    pisitools.remove("/usr/share/netbeans/bin/netbeans.exe")
    pisitools.remove("/usr/share/netbeans/bin/netbeans64.exe") 