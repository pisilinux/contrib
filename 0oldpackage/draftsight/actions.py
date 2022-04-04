#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    shelltools.system("rpm2targz -v %s/download-linux-fedora" %get.workDIR())
    shelltools.system("tar xfvz %s/download-linux-fedora.tar.gz" %get.workDIR())

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/var/", "./var/*")

    pisitools.dohtml("%s/opt/dassault-systemes/DraftSight/Eula/english/*.htm" %get.workDIR())
