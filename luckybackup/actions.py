#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

def setup():
    pisitools.dosed("menu/luckybackup-kde-su.desktop", "^(Exec=)(\/usr\/bin\/luckybackup)", r"\1xdg-su -c \2")
    pisitools.dosed("menu/luckybackup-kde-su.desktop", "^(X-KDE-SubstituteUID=)true", r"\1false")
    qt5.configure()

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.remove("/usr/share/applications/luckybackup-gnome-su.desktop")
