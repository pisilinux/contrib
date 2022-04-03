#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."
NoStrip = ["/"]

def install():
    pisitools.dodir ("/opt/anydesk")
    pisitools.insinto("/opt/anydesk", "anydesk-6.1.1/*")
    pisitools.insinto("/usr/share/polkit-1/actions", "anydesk-6.1.1/polkit-1/com.anydesk.anydesk.policy")
    pisitools.insinto("/etc/init.d", "anydesk-6.1.1/init/anydesk")
    pisitools.dosym("/opt/anydesk/anydesk", "/usr/bin/anydesk")
