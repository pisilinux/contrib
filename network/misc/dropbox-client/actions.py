#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "%s/.dropbox-dist/dropbox-lnx.x86_64-162.4.5419" % get.ARCH()
WorkDir = "/.dropbox-dist/dropbox-lnx.x86_64-188.4.6302"
NoStrip = "/opt/dropbox/library.zip"

def install():
    #pisitools.dodir("/opt/dropbox")
    pisitools.insinto("/opt/dropbox", "*")
    pisitools.dosym("/opt/dropbox/dropboxd", "/usr/bin/dropbox")

    # Arch removes this lib, Pardus libgcc package provides libstdc++.so.6
    #pisitools.remove("/opt/dropbox/libstdc++.so.6")

    pisitools.dodoc("VERSION")
    pisitools.remove("/opt/dropbox/VERSION")

    # you can remove these lines if u don't like monochromatic systemtry icons
    # i'm going to try find a way to make this optional
    #pisitools.insinto("/opt/dropbox/icons/hicolor/16x16/status", "../../hede/*.png")
