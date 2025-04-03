#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/Cursor")
    pisitools.doexe("Cursor-0.48.7-x86_64.AppImage", "/opt/Cursor")
    pisitools.dosym("/opt/Cursor-0.48.7-x86_64.AppImage", "/usr/bin/Cursor")
   