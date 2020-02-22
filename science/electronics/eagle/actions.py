#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
NoStrip = ["/opt/eagle-9.5.2"]

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    pisitools.insinto("/opt/eagle-9.5.2", "*") 
    pisitools.dosym("/opt/eagle-9.5.2/eagle", "/usr/bin/eagle")
