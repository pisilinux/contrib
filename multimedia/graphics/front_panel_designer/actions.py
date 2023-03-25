#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/Front-Panel-Design")
    pisitools.doexe("FrontDesign-US-6.3.6-amd64.AppImage", "/opt/Front-Panel-Design")
    pisitools.dosym("/opt/Front-Panel-Design/runfpd.sh", "/usr/bin/Front-Panel-Design")
   