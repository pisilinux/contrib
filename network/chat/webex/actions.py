#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("ar xf Webex.deb")
    shelltools.system("tar xf data.tar.xz")


def install():
    pisitools.insinto("/opt/Webex", "opt/Webex/*")   