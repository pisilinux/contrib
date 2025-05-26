#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools

Version = get.srcVERSION()


def install():
    pisitools.insinto("/opt/pencil/", "*")
    pisitools.dosym("/opt/pencil/pencil", "/usr/bin/pencil")
