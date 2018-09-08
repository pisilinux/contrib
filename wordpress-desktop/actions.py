#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/wpcom/", "./share/wpcom/*")
    #pisitools.insinto("/usr/bin/", "./share/wpcom/wpcom")    
    #pisitools.insinto("/usr/share/pixmaps/", "./share/pixmaps/wpcom.png")       
    #pisitools.insinto("/usr/share/applications/", "./share/applications/*")
    #pisitools.insinto("/usr/share/doc/atom", "./usr/share/doc/atom/*")
