#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for dirs in ("/usr/share/viber/", "/usr/bin/viber"):
        os.system("/bin/chmod -R 777 %s" % dirs)
