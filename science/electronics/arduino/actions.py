#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
NoStrip = ["/opt/arduino-1.8.12"]

def install():
    pisitools.insinto("/opt/arduino-1.8.12", "*") 
    pisitools.dosym("/opt/arduino-1.8.12/arduino", "/usr/bin/arduino")
