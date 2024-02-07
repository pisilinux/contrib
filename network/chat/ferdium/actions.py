#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.dodir ("/opt/Ferdium")
    pisitools.insinto("/opt/Ferdium", "Ferdium-linux-6.7.0/*")
    pisitools.dosym("/opt/Ferdium/ferdium", "/usr/bin/ferdium")

    
   