#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

Version = get.srcVERSION()
Install = 'arduino-'+Version
WorkDir = "."
NoStrip = ["/"]


def setup():
    shelltools.system("pwd")
    #shelltools.system("wget https://downloads.arduino.cc/arduino-ide/arduino-ide_2.2.1_Linux_64bit.zip")
    shelltools.system("unzip arduino-ide_%s_Linux_64bit.zip" % Version)

def install():
    pisitools.insinto("/opt/arduino/" , "arduino-ide_%s_Linux_64bit/*" % Version) 
    pisitools.dosym("/opt/arduino/arduino-ide", "/usr/bin/arduino")
