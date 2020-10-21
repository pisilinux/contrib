#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

Workdir="."

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/lib/zotero")
    pisitools.insinto("/usr/lib/zotero/", "*")
    pisitools.dosym("/usr/lib/zotero/zotero", "/usr/bin/zotero")

    ## Copy zotero icons to a standard location
    pisitools.domove("/usr/lib/zotero/chrome/icons/default/default16.png", "/usr/share/icons/hicolor/16x16/apps", "zotero.png")
    pisitools.domove("/usr/lib/zotero/chrome/icons/default/default32.png", "/usr/share/icons/hicolor/32x32/apps", "zotero.png")
    pisitools.domove("/usr/lib/zotero/chrome/icons/default/default48.png", "/usr/share/icons/hicolor/48x48/apps", "zotero.png")
    pisitools.domove("/usr/lib/zotero/chrome/icons/default/default256.png", "/usr/share/icons/hicolor/256x256/apps", "zotero.png")
