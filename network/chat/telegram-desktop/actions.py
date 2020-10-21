#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools


def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf tsetup.%s.tar.xz" % get.srcVERSION())


def install():
    pisitools.insinto("/opt/telegram-desktop/", "Telegram/*")
    pisitools.dosym("/opt/telegram-desktop/Telegram","/usr/bin/telegram-desktop")
