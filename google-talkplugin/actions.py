#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/old-licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "x86_64"

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True


def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf google-talkplugin_5.41.0.0-1_amd64.deb")
    shelltools.system("tar xvf data.tar.*")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    pisitools.removeDir("/opt/google/chrome-unstable")
    pisitools.removeDir("/opt/google/chrome-beta")   
