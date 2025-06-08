#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def install():
    pisitools.insinto("/opt/mattermost/", "mattermost-desktop-5.6.0-linux-x64/*")
    pisitools.dosym('/opt/mattermost/mattermost-desktop', '/usr/bin/mattermost-desktop')