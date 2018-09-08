#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    qt5.configure("Webcamoid.pro")

def build():
     qt5.make()

def install():            
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())    

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING.md", "COPYING", "README.md")    
    
