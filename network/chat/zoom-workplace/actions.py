#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools
NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/zoom")
    pisitools.doexe("Zoom_Workplace-6.4.3.827.glibc2.27-x86_64.AppImage", "/opt/zoom")
    pisitools.dosym("/opt/zoom/Zoom_Workplace-6.4.3.827.glibc2.27-x86_64.AppImage", "/usr/bin/zoom")
