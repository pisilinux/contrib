#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #shelltools.system("./config.sh --prefix=/usr --without-win32")
    shelltools.system("./config.sh --without-curses --without-kde4 --without-qt")
    pisitools.dosed("mpsl/Makefile",
                    "$(CFLAGS) -L. -lmpsl",
                    "$(CFLAGS) -lpthread -L. -lmpsl")

def build():
    autotools.make()

def install():
    shelltools.makedirs("%s/usr/bin" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
