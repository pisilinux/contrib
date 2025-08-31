# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Tailscale node agent",
                 "tr": "Tailscale düğüm aracısı"})
serviceDefault = "on"

PIDFILE="/run/tailscale/tailscaled.pid"

@synchronized
def start():
    # path to executable
    # creates a pid file, sets the working directory and calls the jar file
    startService(command="/usr/bin/tailscaled-comar-compat.sh",
                 args="",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
        os.system("/usr/bin/tailscaled --cleanup")
    except:
        pass

def ready():
    start()

def status():
    return isServiceRunning(pidfile=PIDFILE)
