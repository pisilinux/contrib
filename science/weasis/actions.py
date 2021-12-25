#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.dodir("/opt/weasis/weasis")
    pisitools.dodir("/opt/weasis")
    shelltools.system("cp -r ../weasis/*  %s/opt/weasis/weasis" % get.installDIR())
    shelltools.system("cp -r ../viewer-linux.sh  %s/opt/weasis/" % get.installDIR())
    pisitools.dosym("/opt/weasis/viewer-linux.sh", "/usr/bin/weasis")
   
