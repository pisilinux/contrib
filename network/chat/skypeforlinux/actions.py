#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]


def setup():
    shelltools.system("ar xf skypeforlinux_%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.xz")


def install():
    pisitools.insinto("/", "usr")
