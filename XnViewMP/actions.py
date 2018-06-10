#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/bin", "XnView/xnview.sh")
    pisitools.insinto("/opt", "XnView")
    pisitools.insinto("/usr/share/applications", "XnView/XnView.desktop")
    pisitools.insinto("/usr/share/doc", "XnView/license.txt")
    
