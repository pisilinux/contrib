#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf Ramme_3.2.3_amd64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.dosym("/opt/Ramme/ramme", "/usr/bin/ramme")
    pisitools.dosym("/usr/share/icons/hicolor/512x512/apps/ramme.png", "/usr/share/icons/hicolor/scalable/apps/ramme.png")
