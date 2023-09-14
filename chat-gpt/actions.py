#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("tar -xvf ChatGPT_1.1.0_linux_x86_64.AppImage.tar.gz")

def install():
    pisitools.dodir ("/opt/chat-gpt")
    pisitools.doexe("chat-gpt_1.1.0_amd64.AppImage", "/opt/chat-gpt")
    pisitools.dosym("/opt/chat-gpt/chat-gpt_1.1.0_amd64.AppImage", "/usr/bin/chat-gpt")
   
