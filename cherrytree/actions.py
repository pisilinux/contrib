#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("XDG_DATA_HOME", get.workDIR())
shelltools.export("XDG_CONFIG_HOME", get.workDIR())
shelltools.export("XDG_DATA_DIRS", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()


