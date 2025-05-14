#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools


def install():
    pisitools.insinto("/opt/zen-browser/", "*")
    pisitools.dosym("/opt/zen-browser/zen-bin","/usr/bin/zen-bin")
