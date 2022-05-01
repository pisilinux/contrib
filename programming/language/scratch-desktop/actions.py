#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."
NoStrip = ["/"]

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf scratch-desktop_%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.xz")


def install():
    
    pisitools.dodir ("/opt/scratch-desktop")
    pisitools.insinto("/opt/scratch-desktop", "usr/lib/scratch-desktop/*")
    pisitools.dosym("/opt/scratch-desktop/electron", "/usr/bin/scratch-desktop")
