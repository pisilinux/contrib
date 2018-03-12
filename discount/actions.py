#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf discount_2.2.3b8-2_amd64.deb")
    shelltools.system("tar -xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.remove("/usr/share/doc/discount/changelog.Debian.gz")
