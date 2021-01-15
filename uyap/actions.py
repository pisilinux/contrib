#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir="."
def setup():
    #shelltools.system("ar xf uyappardus.zip")
    shelltools.system("ar xvf uyap_pardus_5_0_2_amd64/uyapeditor_5.0.2_amd64.deb")
    shelltools.system("tar xvf data.tar.xz")

def install():
    pisitools.insinto("/usr", "%s/usr/*" % get.workDIR())

    #fixed the authentication problem.
    shelltools.system("chmod -R 0755 %s/usr/share/UYAPEditor/*" % get.installDIR())

    #UYAPEditor has singing problem with java-8. For now 
    #pisitools.dosed("%s/usr/share/UYAPEditor/dokuman.sh" % get.installDIR(), "java", "java_8")
    #pisitools.dosed("%s/usr/share/UYAPEditor/sablon.sh" % get.installDIR(), "java", "java_8")
