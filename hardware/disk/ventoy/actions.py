#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/usr", "/opt"]

def install():
    pisitools.insinto("/opt/ventoy", "./*")
    #pisitools.dosym("/opt/ventoy/VentoyGUI.x86_64", "/usr/bin/ventoy")
    #pisitools.insinto("/usr/share/applications", "./usr/share/applications/gitbook-editor.desktop")
    #pisitools.insinto("/usr/share/pixmaps", "./opt/gitbook-editor/gitbook.png")
