#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True


def setup():
    shelltools.system("ar xf spotify-client_%s.*_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.gz")


def install():
    pisitools.insinto("/", "usr")
    pisitools.dosym("/usr/lib/libcurl.so", "/usr/lib/libcurl-gnutls.so.4") 
