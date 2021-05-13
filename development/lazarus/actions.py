#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os



def build():
    autotools.make("clean all")

def install():
    autotools.rawInstall('PREFIX="%s/usr"' % (get.installDIR()))




