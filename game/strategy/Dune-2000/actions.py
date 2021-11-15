#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/dune2")
    pisitools.doexe("OpenRA-Dune-2000-x86_64.AppImage", "/opt/dune2")
    pisitools.dosym("/opt/dune2/OpenRA-Dune-2000-x86_64.AppImage", "/usr/bin/dune2")
    #pisitools.dosym("/usr/share/icons/hicolor/1024x1024/apps/franz.png", "/usr/share/icons/hicolor/scalable/apps/franz.png")
