#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir="."
def setup():
    #shelltools.system("ar xf uyappardus.zip")
    shelltools.system("ar xvf uyap_pardus_4_2_9_amd64/uyapeditor_4.2.9_amd64.deb")
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/usr", "%s/usr/*" % get.workDIR())
    #For java_8
    pisitools.dosed("%s/usr/share/UYAPEditor/dokuman.sh" % get.installDIR(), "java", "java_8")
    pisitools.dosed("%s/usr/share/UYAPEditor/sablon.sh" % get.installDIR(), "java", "java_8")
    shelltools.system("chmod -R 0755 %s/usr/share/UYAPEditor/*" % get.installDIR())
