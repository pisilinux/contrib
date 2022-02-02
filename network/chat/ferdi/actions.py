#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/Ferdi")
    pisitools.doexe("Ferdi-5.7.0.AppImage", "/opt/Ferdi")
    pisitools.dosym("/opt/Ferdi/Ferdi-5.7.0.AppImage", "/usr/bin/ferdi")
   