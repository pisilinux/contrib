from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "teamviewer Remote Control Application",
    "tr": "teamviewer Uzak Masaüstü Bağlantısı"})

serviceDefault = "on"

PIDFILE="/run/teamviewerd.pid"
DAEMON ="/opt/teamviewer/tv_bin/teamviewerd"

@synchronized
def start():
    startService(command=DAEMON,
                 args=" -d",
                 donotify=True)
    os.system("pidof -o %PPID " + "%s > %s" % (DAEMON, PIDFILE))

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(pidfile=PIDFILE)
