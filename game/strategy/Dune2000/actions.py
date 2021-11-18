#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/Dune2")
    pisitools.doexe("OpenRA-Dune-2000-x86_64.AppImage", "/opt/Dune2")
    pisitools.dosym("/opt/Dune2/OpenRA-Dune-2000-x86_64.AppImage", "/usr/bin/Dune2000")
   