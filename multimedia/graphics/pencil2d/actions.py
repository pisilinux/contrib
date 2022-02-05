#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/pencil2d")
    pisitools.doexe("pencil2d-linux-amd64-0.6.6.AppImage", "/opt/pencil2d")
    pisitools.dosym("/opt/pencil2d/pencil2d-linux-amd64-0.6.6.AppImage", "/usr/bin/pencil2d")
   