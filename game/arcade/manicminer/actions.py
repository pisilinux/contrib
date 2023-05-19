#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("unzip ManicMinerV17aLinux.zip")

def install():
    pisitools.insinto( "/opt/", "ManicMiner/")
    pisitools.dosym("/opt/ManicMiner/ManicMinerLinux64", "/usr/bin/ManicMiner")