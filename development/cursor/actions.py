#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True
Version = get.srcVERSION()


def install():
    pisitools.dodir ("/opt/Cursor")
    pisitools.doexe("Cursor-%s-x86_64.AppImage" % Version, "/opt/Cursor")
    pisitools.dosym("/opt/Cursor/Cursor-%s-x86_64.AppImage" % Version, "/usr/bin/cursor")
   