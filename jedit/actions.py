#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

JEDIT_HOME="%s/usr/share/jedit" % get.installDIR()

def install():
    #shelltools.system("java -jar jedit5.3pre1install.jar auto /usr/share/java/jedit unix-script=/usr/bin unix-man=/usr/share/man")
   shelltools.system("java -jar jedit5.3.0install.jar auto %s/usr/share/jedit unix-script=%s/usr/bin unix-man=%s/usr/share/man" % (get.installDIR(), get.installDIR(), get.installDIR()))

