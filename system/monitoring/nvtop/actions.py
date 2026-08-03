#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# WorkDir = "nvtop-3.3.2"

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(
        "-DCMAKE_INSTALL_PREFIX=/usr \
         -DCMAKE_BUILD_TYPE=Release \
         -DNVIDIA_SUPPORT=ON \
         -DAMDGPU_SUPPORT=ON \
         -DINTEL_SUPPORT=ON \
         -DMSM_SUPPORT=ON",
        sourceDir=".."
    )

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())