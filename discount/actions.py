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
    shelltools.system("ar xf discount_2.1.7-1_amd64.deb")
    shelltools.system("tar -xzf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.remove("/usr/share/doc/discount/changelog.Debian.gz")
