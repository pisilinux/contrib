# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Arksigner Daemon",
                 "tr": "Arksigner Daemon"})
serviceDefault = "on"

PIDFILE="/run/arksignerd.pid"

@synchronized
def start():
    # path to executable
    # creates a pid file, sets the working directory and calls the jar file
    startService(command="/etc/init.d/arksignerd",
                 args="start",
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
