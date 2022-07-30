#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/koodo-reader")
    pisitools.doexe("Koodo-Reader-1.4.5.AppImage", "/opt/koodo-reader")
    pisitools.dosym("/opt/koodo-reader/Koodo-Reader-1.4.5.AppImage", "/usr/bin/koodo-reader")
