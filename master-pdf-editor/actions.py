#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/share/pixmaps/", "masterpdfeditor3.png")
    pisitools.insinto("/usr/share/applications/", "masterpdfeditor3.desktop")
    pisitools.dodir("/opt/master-pdf-editor-3")
    pisitools.insinto("/opt/master-pdf-editor-3/lang","lang/*.qm")
    pisitools.insinto("/opt/master-pdf-editor-3/lang","lang/*.ts")
    pisitools.insinto("/usr/bin/","masterpdfeditor3")
    
    pisitools.dodoc("license.txt")
    