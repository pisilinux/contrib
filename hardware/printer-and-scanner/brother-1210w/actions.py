#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("rpm2targz -v %s/hl1210wlpr-3.0.1-1.i386.rpm" %get.workDIR())
    shelltools.system("rpm2targz -v %s/hl1210wcupswrapper-3.0.1-1.i386.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/hl1210wlpr-3.0.1-1.i386.tar.gz" %get.workDIR())
    shelltools.system("tar xfvz %s/hl1210wcupswrapper-3.0.1-1.i386.tar.gz" %get.workDIR())

def install():
    pisitools.dodir("/usr/share/cups/model")
    pisitools.dodir("/usr/lib/cups/filter")
    pisitools.dodir("/opt")
    pisitools.insinto("/usr/share/cups/model","%s/opt/brother/Printers/HL1210W/cupswrapper/brother-HL1210W-cups-en.ppd" % get.workDIR())
    pisitools.insinto("/usr/lib/cups/filter","%s/opt/brother/Printers/HL1210W/cupswrapper/brother_lpdwrapper_HL1210W" % get.workDIR())
    pisitools.insinto("/opt", "opt/*")
