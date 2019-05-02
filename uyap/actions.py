#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/applications/", "usr/share/applications/*.desktop")
    pisitools.insinto("/usr/share/", "usr/share/UYAPEditor")
    pisitools.insinto("/usr/share/", "usr/share/icons")
    pisitools.insinto("/usr/share/", "usr/share/mime")
