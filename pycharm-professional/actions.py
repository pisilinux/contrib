#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    #shutil.rmtree("pycharm-2018.1.4/jre")
    pisitools.insinto("/opt/pycharm", "pycharm-2018.1.4/*")
    pisitools.dosym("/opt/pycharm/bin/pycharm.sh", "/usr/bin/pycharm")