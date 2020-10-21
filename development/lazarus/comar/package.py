#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("$THEPREFIX/usr/lib64/fpc/3.0.4/samplecfg $THEPREFIX/usr/lib64/fpc/3.0.4 $ETCDIR")
