#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools


def setup():
    shelltools.system("pwd")

    shelltools.system("unzip brave-browser-nightly-1.18.8-linux-amd64.zip")


def install():
    pisitools.insinto("/opt/brave-browser/", "*")
    pisitools.dosym("/opt/brave-browser/brave","/usr/bin/brave-browser")
