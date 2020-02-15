#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools



def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf utopia-latest.amd64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
	pisitools.insinto("/opt/utopia/", "/*")
    #pisitools.insinto("/", "opt")
