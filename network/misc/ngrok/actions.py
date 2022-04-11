#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools


def setup():
    shelltools.system("pwd")
    shelltools.system("unzip ngrok-stable-linux-amd64.zip")
   
def install():
    pisitools.insinto("/opt/ngrok", "ngrok")
    pisitools.dosym("/opt/ngrok/ngrok", "/usr/bin/ngrok")