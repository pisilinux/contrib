#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import pisitools

#WorkDir="musique"

def setup():
    pisitools.dosed("musique.desktop", "=minitunes",  "=musique")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()
    pisitools.insinto("/usr/share/pixmaps/musique.png",  "images/app.png")
    pisitools.dodoc("README.md",  "COPYING")





