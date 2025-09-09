#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("unzip odin.zip")
    shelltools.system("chmod +x odin4")

def install():
    pisitools.insinto("/usr/bin", "odin4")
