#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf spotify-client_%s.*_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    #pisitools.dosym("/usr/share/spotify/spotify.desktop", "/usr/share/applications/spotify.desktop")
    #pisitools.dosym("/usr/share/libffado/icons/hi64-apps-ffado.png", "/usr/share/pixmaps/ffado-mixer.png")
