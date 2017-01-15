#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
#from pisi.actionsapi import pisitools

WorkDir="qt5-fsarchiver-0.6.19-20.1/qt5-fsarchiver"

def setup():
    #shelltools.system("qmake-qt5")
    shelltools.system("qmake-qt5 qt5-fsarchiver.pro")
    #qt5.configure("qmake-qt5")

def build():
    qt5.make()

def install():
    qt5.install()


#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")
