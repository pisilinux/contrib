#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "."

def setup():
    shelltools.system("pwd")
    shelltools.system("tar -xf teamviewer_14.5.1691_amd64.tar.xz")

def install():
    pisitools.insinto("~/teamviewer/", "teamviewer/*")
    pisitools.dosym("~/teamviewer/tv_bin/TeamViewer", "/usr/bin/teamviewer")
