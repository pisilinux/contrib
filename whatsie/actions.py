#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr", "/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf whatsie-2.0.18-linux-amd64.deb")
    shelltools.system("tar -xzf data.tar.gz")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    pisitools.insinto("usr/share/doc/whatsie", "/opt/whatsie/LICENSE")
    pisitools.insinto("usr/share/doc/whatsie", "/opt/whatsie/LICENSES.chromium.html")
    pisitools.remove("/usr/share/doc/whatsie/changelog.gz")
