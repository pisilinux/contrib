#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    pisitools.insinto("/opt/VSCode-linux-x64", "./*")
    pisitools.dosym("/opt/VSCode-linux-x64/bin/code", "/usr/bin/code")
