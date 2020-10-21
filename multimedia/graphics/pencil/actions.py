#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf pencil_"+Version+".ga_amd64.deb")
    shelltools.system("tar xf data.tar.gz")
    

def install():
    pisitools.insinto("/opt/pencil-3.1.0.ga/", "opt/pencil-3.1.0.ga/*")
    pisitools.dosym("/opt/pencil-3.1.0.ga/pencil", "/usr/bin/pencil")
