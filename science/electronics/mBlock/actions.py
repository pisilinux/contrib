#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf mBlock-4.0.0-linux-4.0.0.tar.gz")

def install():
    pisitools.insinto("/opt/mBlock/", "mBlock/*")
    pisitools.dosym("/opt/mBlock/mBlock", "/usr/bin/mBlock")
