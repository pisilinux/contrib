#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("pwd")
    shelltools.system("tar -xJf code-stable-vscode-amd64.tar.xz")        
def install():
    #shelltools.cd("")
    pisitools.insinto("/opt/vs-code-editor", "./VSCode-linux-x64/*")
    #pisitools.insinto("/usr/bin", "./VSCode-linux-x64/code")
