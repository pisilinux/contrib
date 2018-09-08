#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/opt/teamviewer/tv_bin/wine/drive_c/TeamViewer/tvwine.dll.so"]

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf teamviewer_13.0.9865_amd64.deb")
    shelltools.system("tar xf data.tar.xz")
    
def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/etc/systemd/system", "./opt/teamviewer/tv_bin/script/teamviewerd.service")
    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer/tv_bin/teamviewerd", "etc/init.d/teamviewerd")
    pisitools.dosym("/opt/teamviewer/tv_bin/script/teamviewer", "usr/bin/teamviewer")
    pisitools.dosym("/opt/teamviewer/logfiles", "var/log/teamviewer")
    pisitools.dosym("/opt/teamviewer/config", "etc/teamviewer")
    
    pisitools.dodoc("%s/opt/teamviewer/doc/License.txt" %get.workDIR())
    
    
    shelltools.chmod("%s/opt/teamviewer/doc/*" % get.installDIR(),0755)
    shelltools.chmod("%s/opt/teamviewer/tv_bin/*" % get.installDIR(),0755)  
    

    
    
    
    
