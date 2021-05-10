#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
   # shelltools.system("pwd")
    shelltools.system("ar xf vivaldi-stable_%s-1_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/opt/", "opt/vivaldi*")
    pisitools.dosym("/opt/vivaldi/vivaldi", "/usr/bin/vivaldi")