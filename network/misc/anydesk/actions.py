#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."
NoStrip = ["/"]
Version = get.srcVERSION()

def install():
    pisitools.dodir ("/opt/anydesk")
    pisitools.insinto("/opt/anydesk", "anydesk-"+Version+"/*")
    pisitools.insinto("/usr/share/polkit-1/actions", "anydesk-"+Version+"/polkit-1/com.anydesk.anydesk.policy")
    pisitools.insinto("/etc/init.d", "anydesk-"+Version+"/init/anydesk")
    pisitools.dosym("/opt/anydesk/anydesk", "/usr/bin/anydesk")
