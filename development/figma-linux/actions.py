#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

#WorkDir = "."
#NoStrip = ["/"]

def setup():
    shelltools.system("pwd")
    shelltools.system("unzip figma-linux_%s_linux_amd64.zip" % get.srcVERSION())

def install():
    #pisitools.dodir ("/opt/figma-linux")
    pisitools.insinto("/opt/figma-linux", "*")
    pisitools.dosym("/opt/figma-linux/figma-linux", "/usr/bin/figma-linux")
    #pisitools.insinto("/usr/share/polkit-1/actions", "anydesk-6.1.1/polkit-1/com.anydesk.anydesk.policy")
    #pisitools.insinto("/etc/init.d", "anydesk-6.1.1/init/anydesk")
