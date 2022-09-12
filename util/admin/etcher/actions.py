#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/etcher")
    pisitools.doexe("balenaEtcher-1.7.3-x64.AppImage", "/opt/etcher")
    pisitools.dosym("/opt/etcher/balenaEtcher-1.7.3-x64.AppImage", "/usr/bin/etcher")