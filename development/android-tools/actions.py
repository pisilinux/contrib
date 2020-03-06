#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("unzip platform-tools_r29.0.5-linux.zip")

def install():
    pisitools.insinto("/usr/bin/", "platform-tools/adb")
    pisitools.insinto("/usr/bin/", "platform-tools/fastboot")
