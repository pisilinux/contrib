#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools, shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


WorkDir = '.'


def setup():
    pass


def build():
    pass


def install():
    pisitools.insinto('/opt', 'zoom')
    pisitools.dosym('/opt/zoom/ZoomLauncher', '/usr/bin/zoom')
