#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
NoStrip = ["/"]

Release = "-1"

def setup():
    shelltools.system("ar xf %s/google-chrome-stable_%s%s_amd64.deb" % (get.workDIR(), get.srcVERSION(), Release))
    shelltools.system("tar xvf %s/data.tar.xz --exclude=usr/share/gnome-control-center --exclude=usr/bin --exclude=etc" %get.workDIR())
    shelltools.chmod(get.workDIR() + "/opt/google/chrome/*", 0755)

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/usr/", "./usr/*")
    shelltools.system("chmod -v 4755 %s/opt/google/chrome/chrome-sandbox" %get.installDIR())
    pisitools.dosym("/opt/google/chrome/google-chrome", "/usr/bin/google-chrome-stable")
    #pisitools.dosym("/opt/google/chrome/google-chrome.desktop", "/usr/share/applications/google-chrome.desktop")
    pisitools.dosym("/opt/google/chrome/product_logo_32.xpm", "/usr/share/pixmaps/google-chrome.xpm")
    pisitools.dosym("/opt/google/chrome/product_logo_256.png", "/usr/share/pixmaps/google-chrome.png")
    pisitools.dosym("/usr/lib/nss/libnss3.so", "/usr/lib/libnss3.so.1d")
    pisitools.dosym("/usr/lib/nss/libnssutil3.so", "/usr/lib/libnssutil3.so.1d")
    pisitools.dosym("/usr/lib/nss/libsmime3.so", "/usr/lib/libsmime3.so.1d")
    pisitools.dosym("/usr/lib/nss/libssl3.so", "/usr/lib/libssl3.so.1d")
    pisitools.dosym("/usr/lib/libplds4.so", "/usr/lib/libplds4.so.0d")
    pisitools.dosym("/usr/lib/libplc4.so", "/usr/lib/libplc4.so.0d")
    pisitools.dosym("/usr/lib/libnspr4.so", "/usr/lib/libnspr4.so.0d")
    pisitools.dosym("/lib/libbz2.so", "/usr/lib/libbz2.so.1.0")
    pisitools.dosym("/usr/lib/libudev.so", "/opt/google/chrome/libudev.so.0")
