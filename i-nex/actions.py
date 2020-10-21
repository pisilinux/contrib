#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools


def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf i-nex_7.6.0-0-bzr977-20161012-ubuntu16.10.1_amd64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
   pisitools.insinto("/", "usr")
