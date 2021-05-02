#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get, pisitools, shelltools





def install():
    pisitools.insinto("/usr/share/eclipse", "./*")
