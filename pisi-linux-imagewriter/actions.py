#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt5

def setup():    
    qt5.configure("PisiImageWriter.pro")

def build():
    qt5.make()

def install():
    qt5.install()
    pisitools.insinto("/usr/bin/", "PisiImageWriter")
    pisitools.insinto("/usr/share/doc/pisi-linux-imagewriter", "doc")

    pisitools.dodoc( "README.md")
