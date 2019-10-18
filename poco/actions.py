#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools, shelltools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs('build')
    shelltools.cd('build')
    parameters = " ".join([
        "-DCMAKE_BUILD_TYPE=Release",
    ])
    cmaketools.configure(parameters=parameters, sourceDir='..')


def build():
    shelltools.cd('build')
    cmaketools.make()


def install():
    shelltools.cd('build')
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
