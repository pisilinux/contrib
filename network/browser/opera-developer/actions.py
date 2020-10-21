#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
   # shelltools.system("pwd")
    shelltools.system("ar xf opera-developer_%s_amd64.deb" %get.srcVERSION())
    shelltools.system("tar xvf data.tar.xz")

def install():
    # root owns sandbox as it is setuid
    shelltools.system("chown root:root usr/lib/x86_64-linux-gnu/opera-developer/opera_sandbox")
    # ensure setuid
    shelltools.system("chmod 4755 usr/lib/x86_64-linux-gnu/opera-developer/opera_sandbox")
    pisitools.insinto("/", "usr")

    # Because ew.
    pisitools.move("%s/usr/lib/x86_64-linux-gnu/*" % get.installDIR(), "%s/usr/lib" % get.installDIR())
    pisitools.dosym("/usr/lib/opera-developer/libffmpeg.so", "/usr/lib/libffmpeg.so")
    pisitools.removeDir("/usr/lib/x86_64-linux-gnu")
    pisitools.removeDir("/usr/share/lintian")

    pisitools.remove("/usr/bin/opera-developer")
    pisitools.insinto("/usr/bin/", "./usr/lib/x86_64-linux-gnu/opera-developer/opera-developer")
