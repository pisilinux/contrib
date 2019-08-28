#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."


def setup():
    shelltools.system("pwd")
    shelltools.system("tar -xf teamviewer_14.5.1691_amd64.tar.xz")
    
def install():
    pisitools.insinto("/opt/teamviewer/", "teamviewer/*")
    pisitools.insinto("/etc/systemd/system", "teamviewer/tv_bin/script/teamviewerd.service")
    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer/tv_bin/teamviewerd", "etc/init.d/teamviewerd")
    pisitools.dosym("/opt/teamviewer/tv_bin/script/teamviewer", "usr/bin/teamviewer")
    pisitools.dosym("/opt/teamviewer/logfiles", "var/log/teamviewer")
    pisitools.dosym("/opt/teamviewer/config", "etc/teamviewer")
    
    pisitools.dodoc("%s/teamviewer/doc/License.txt" %get.workDIR())
    
    
    shelltools.chmod("%s/opt/teamviewer/doc/*" % get.installDIR(),0755)
    shelltools.chmod("%s/opt/teamviewer/tv_bin/*" % get.installDIR(),0755)

