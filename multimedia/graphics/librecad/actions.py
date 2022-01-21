#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/LibreCAD")
    pisitools.doexe("LibreCAD-2.2.0-rc3-21-g5d331c8b-x86_64.AppImage", "/opt/LibreCAD")
    pisitools.dosym("/opt/LibreCAD/LibreCAD-2.2.0-rc3-21-g5d331c8b-x86_64.AppImage", "/usr/bin/LibreCAD")
   