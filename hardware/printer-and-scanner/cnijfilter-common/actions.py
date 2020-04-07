#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

def install():

    pisitools.insinto("/usr/lib/cups/backend", "./lib64/cups/backend/*")
    pisitools.insinto("/usr/lib/cups/filter", "./lib64/cups/filter/pstocanonij")

    pisitools.dobin("./local/bin/cngpij", "/usr/local/bin/")

    pisitools.insinto("usr/share/doc", "./share/doc/cnijfilter-common-3.40/LICENSE-cnijfilter-3.40EN.txt")
    pisitools.insinto("usr/share/doc","./share/doc/cnijfilter-common-3.40/LICENSE-cnijfilter-3.40FR.txt")
    pisitools.insinto("usr/share/doc","./share/doc/cnijfilter-common-3.40/LICENSE-cnijfilter-3.40JP.txt")
    pisitools.insinto("usr/share/doc","./share/doc/cnijfilter-common-3.40/LICENSE-cnijfilter-3.40SC.txt")

