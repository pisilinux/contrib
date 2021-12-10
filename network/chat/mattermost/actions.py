#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir ("/opt/Mattermost")
    pisitools.doexe("mattermost-desktop-5.0.2-linux-x86_64.AppImage", "/opt/Mattermost")
    pisitools.dosym("/opt/Mattermost/mattermost-desktop-5.0.2-linux-x86_64.AppImage", "/usr/bin/mattermost")
   