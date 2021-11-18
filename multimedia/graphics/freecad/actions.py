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
    pisitools.doexe("FreeCAD_0.19-24291-Linux-Conda_glibc2.12-x86_64.AppImage", "/opt/FreeCAD")
    pisitools.dosym("/opt/FreeCAD/FreeCAD_0.19-24291-Linux-Conda_glibc2.12-x86_64.AppImage", "/usr/bin/FreeCAD")
   