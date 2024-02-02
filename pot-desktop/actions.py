#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/Pot-Desktop")
    pisitools.doexe("pot_2.7.4_amd64.AppImage", "/opt/Pot-Desktop")
    pisitools.dosym("/opt/Pot-Desktop/pot_2.7.4_amd64.AppImage", "/usr/bin/Pot-Desktop")
   