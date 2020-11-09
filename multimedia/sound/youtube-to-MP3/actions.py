
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf YouTubeToMP3.amd64.deb")
    shelltools.system("tar xvf data.tar.xz")
def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
