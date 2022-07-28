#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf Koodo.Reader-1.4.5.deb")
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/opt/", "opt/*")
    pisitools.dosym("opt/koodo-reader/koodo-reader", "/usr/bin/koodo-reader")
    pisitools.insinto("/usr/share/applications", "usr/share/applications/koodo-reader.desktop")
    pisitools.insinto("/usr/share/icons/hicolor/256x256/apps", "usr/share/icons/hicolor/256x256/apps/koodo-reader.png")
    pisitools.insinto("/usr/share/mime/packages", "usr/share/mime/packages/koodo-reader.xml")
    pisitools.insinto("/usr/share/doc", "usr/share/doc/koodo-reader")
