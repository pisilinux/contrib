#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir("/opt/SynfigStudio")
    pisitools.doexe("SynfigStudio-1.5.1-2021.10.21-linux64-2cb6c.appimage", "/opt/SynfigStudio")
    pisitools.dosym("/opt/SynfigStudio/SynfigStudio-1.5.1-2021.10.21-linux64-2cb6c.appimage", "/usr/bin/SynfigStudio")
   