#!/usr/bin/python

import os
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools


def setup():
    shelltools.system("$THEPREFIX/usr/lib64/fpc/3.0.4/samplecfg $THEPREFIX/usr/lib64/fpc/3.0.4 $ETCDIR")

