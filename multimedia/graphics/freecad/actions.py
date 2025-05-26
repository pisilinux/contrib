#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/FreeCAD")
    pisitools.doexe("FreeCAD_1.0.1-conda-Linux-x86_64-py311.AppImage", "/opt/FreeCAD")
    pisitools.dosym("/opt/FreeCAD/FreeCAD_1.0.1-conda-Linux-x86_64-py311.AppImage", "/usr/bin/FreeCAD")
   