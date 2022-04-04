#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
def install():
    pisitools.insinto("/usr", "./*")
