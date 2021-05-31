#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s" % get.ARCH()

def install():
    # Define bits variable for 32-bit and 64-bit architectures
    #bits = "amd64" if get.ARCH() == "x86_64" else "i386"

    # Extract Debian package
    shelltools.system("ar xf plexmediaserver_%s-280ab6053_amd64.deb" % get.srcVERSION())

    shelltools.system("tar xf data.tar.xz")

    pisitools.insinto("/usr/share/pixmaps/", "usr/share/pixmaps/plexmediaserver.png")
    pisitools.insinto("/usr/share/applications/", "usr/share/applications/plexmediaserver.desktop")
    pisitools.insinto("/", "etc")
    pisitools.insinto("/usr/", "usr/lib")
    #pisitools.insinto("/usr/", "usr/sbin")

    shelltools.system("service apache start")