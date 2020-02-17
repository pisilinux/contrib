#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get 
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("ar xf wps-office_%s.XA_amd64.deb" %get.srcVERSION())
    shelltools.system("tar xf data.tar.xz")

def build():
    pass

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "etc")
