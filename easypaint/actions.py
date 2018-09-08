#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5

WorkDir = "EasyPaint-0.1.1/sources"

def setup():
    #shelltools.cd("EasyPaint-0.1.1/sources")
    #shelltools.system("lupdate easypaint.pro")
   # shelltools.system("lrelease easypaint.pro")
    qt5.configure("easypaint.pro")

def build():
    qt5.make()

def install():
    qt5.install()

    #pisitools.dodoc("AUTHORS", "THANKS", "COPYING", "README.md")
