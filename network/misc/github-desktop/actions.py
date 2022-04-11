#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf GitHubDesktop-linux-"+Version+"-linux4.deb")
    shelltools.system("tar xf data.tar.xz")
    

def install():
    pisitools.insinto("/opt/github-desktop/", "usr/lib/github-desktop/*")
    pisitools.dosym("/opt/github-desktop/github-desktop", "/usr/bin/github-desktop")