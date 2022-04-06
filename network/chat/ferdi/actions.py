#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.dodir ("/opt/Ferdi")
    pisitools.insinto("/opt/Ferdi", "ferdi-5.8.1/*")
    pisitools.dosym("/opt/Ferdi/ferdi", "/usr/bin/ferdi")

    
   