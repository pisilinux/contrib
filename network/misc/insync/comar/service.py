from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "Insync",
                 "tr": "Insync"})

#serviceConf = "apache2"

PIDFILE = "/run/insync.pid"
DAEMON="/usr/bin/insync start"
DAEMON1="/usr/bin/insync quit"

@synchronized
def start():
     startService(command=DAEMON,
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)
    

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def reload():
    stopService(command="/usr/sbin/insync reload")

def status():
    return isServiceRunning(PIDFILE)