#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf tsetup.1.7.0.tar.xz")

def install():
    pisitools.insinto("/usr/bin/", "Telegram/*")  
