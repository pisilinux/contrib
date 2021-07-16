#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/pycharm-community", "pycharm-community-2021.1.3/*")
    pisitools.dosym("/opt/pycharm-community/bin/pycharm.sh", "/usr/bin/pycharm-community")
