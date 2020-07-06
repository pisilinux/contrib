#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

#from pisi.actionsapi import get
from pisi.actionsapi import pisitools
#from pisi.actionsapi import kde5
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    #kde5.configure("/")
    #shelltools.makedirs("build")
    #shelltools.cd("build")
    cmaketools.configure()

def build():
    #kde5.make()
     cmaketools.make()

def install():
    #kde5.install()
    cmaketools.install()

    pisitools.dodoc("COPYING", "CHANGELOG", "README.md")