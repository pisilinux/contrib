#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get, pisitools, shelltools



def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf atom-amd64.tar.gz")

def install():
    pisitools.insinto("/opt/atom/", "atom-1.57.0-amd64/*")
