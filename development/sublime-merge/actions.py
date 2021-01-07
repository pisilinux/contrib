#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    pisitools.insinto("/opt/sublime_merge","*")

    for i in [16,32,48,128,256]:
        pisitools.domove("/opt/sublime_merge/Icon/{0}x{0}/sublime-merge.png".format(i),"/usr/share/icons/hicolor/{0}x{0}/apps".format(i))

    pisitools.removeDir("/opt/sublime_merge/Icon")    
    

    pisitools.dosym("/opt/sublime_merge/sublime_merge","/usr/bin/sublime_merge")
