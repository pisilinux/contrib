#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

#NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf dcpt510wpdrv-%s-0.i386.deb"  % get.srcVERSION())
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.dodir("/usr/share/cups/model")
    pisitools.dodir("/usr/lib/cups/filter")

    pisitools.insinto("/usr/share/cups/model","%s/opt/brother/Printers/dcpt510w/cupswrapper/brother_dcpt510w_printer_en.ppd" % get.workDIR())
    pisitools.insinto("/usr/lib/cups/filter","%s/opt/brother/Printers/dcpt510w/cupswrapper/brother_lpdwrapper_dcpt510w" % get.workDIR())
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    shelltools.chmod("%s/usr/lib/cups/filter/brother_lpdwrapper_dcpt510w" % get.installDIR(), 4711)
