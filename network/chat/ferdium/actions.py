#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

#WorkDir = "."
#NoStrip = ["/"]
  
NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    
    shelltools.system("ar xf Ferdium-linux-%s-amd64.deb" % get.srcVERSION())
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/opt/", "opt/Ferdium")
    #pisitools.dosym("/opt/vivaldi/vivaldi", "/usr/bin/vivaldi")

    #pisitools.dodir ("/opt/Ferdium")
    #pisitools.insinto("/opt/Ferdium", "Ferdium-linux-6.7.5/*")
    pisitools.dosym("/opt/Ferdium/ferdium", "/usr/bin/ferdium")
