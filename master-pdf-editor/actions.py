#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/share/pixmaps/", "masterpdfeditor4.png")
    pisitools.insinto("/usr/share/applications/", "masterpdfeditor4.desktop")
    pisitools.dodir("/opt/master-pdf-editor-4")
    pisitools.insinto("/opt/master-pdf-editor-4/lang","lang/*.qm")
    pisitools.insinto("/opt/master-pdf-editor-4/lang","lang/*.ts")
    pisitools.insinto("/usr/bin/","masterpdfeditor4")
    
    pisitools.dodoc("license.txt")
    
