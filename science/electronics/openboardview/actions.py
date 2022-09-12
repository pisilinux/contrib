#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
def setup():
    shelltools.system("ar xf openboardview_9.0.3-1_amd64.deb")
    shelltools.system("tar xf data.tar.gz")

def install():    
    pisitools.insinto("/", "usr")
   