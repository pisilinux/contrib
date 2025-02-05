# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "TurksatImza Service",
                 "tr": "TurksatImza Servisi"})
serviceDefault = "off"

PIDFILE="/run/turksat-imza/turksat-imza.pid"

@synchronized
def start():
    # path to executable
    # creates a pid file, sets the working directory and calls the jar file
    startService(command="/usr/share/signNativeOsService/bin/systemctl/start_comar.sh",
                 args="",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def ready():
    start()

def status():
    return isServiceRunning(pidfile=PIDFILE)
