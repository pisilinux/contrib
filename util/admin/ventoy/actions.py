#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.dodir ("/opt/Ventoy")
    pisitools.insinto("/opt/Ventoy", "ventoy-1.0.79/*")
    pisitools.dosym("/opt/Ventoy/VentoyGUI.x86_64", "/usr/bin/Ventoy")
