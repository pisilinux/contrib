#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

#WorkDir = "apfs-fuse-master"

def setup():
    shelltools.system("mv ../lzfse-lzfse-1.0 lzfse")
    shelltools.system("mv lzfse ./3rdparty/")
    shelltools.system("mkdir build")
    shelltools.cd("build")
    shelltools.system("cmake .. -DBUILDCMAKE_SHARED_LIBS:BOOL=OFF -DCMAKE_BUILD_TYPE=Release")

def build():
    shelltools.cd('build')
    cmaketools.make()


def install():
    shelltools.cd('build')
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("LICENSE", "README.md")
