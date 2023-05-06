#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
	shelltools.system("pwd")
	shelltools.system('unzip ACS-Unified-PKG-Lnx-118-P.zip')
	shelltools.system("ar xf ACS-Unified-PKG-Lnx-118-P/debian/buster/libacsccid1_1.1.8-1~bpo10+1_amd64.deb")
	shelltools.system("tar xvf data.tar.xz")

def install():
	pisitools.insinto("/", "usr")
	pisitools.insinto("/", "lib")