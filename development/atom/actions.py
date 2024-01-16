#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf atom-amd64.deb")
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")


"""sumary_line

Keyword arguments:
argument -- description
Return: return_description


def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf atom-amd64.tar.gz")

def install():
    pisitools.insinto("/opt/atom/", "atom-1.57.0-amd64/*")
"""
