#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/onlyoffice")
    pisitools.doexe("DesktopEditors-x86_64.AppImage", "/opt/onlyoffice")
    pisitools.dosym("/opt/onlyoffice/DesktopEditors-x86_64.AppImage", "/usr/bin/onlyoffice")
   