#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools, get


#NoStrip = ["/opt", "/usr"]
#IgnoreAutodep = True

def install():
    pisitools.insinto("/opt/gitkraken/", "*")
    pisitools.dosym('/opt/gitkraken/gitkraken', '/usr/bin/gitkraken')
