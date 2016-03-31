from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "teamviewer Remote Control Application",
    "tr": "teamviewer Uzak Masaüstü Bağlantısı"})

serviceDefault = "on"

pidFile = "/run/teamviewerd.pid"


@synchronized
def start():
    loadEnvironment()
    startService(command="/opt/teamviewer/tv_bin/teamviewerd",
                 args="-d",
                 pidfile=pidFile,
                 makepid=True,
                 donotify=True)
        

@synchronized
def stop():
    stopService(pidfile=pidFile,
                donotify=True)
    os.unlink(pidFile)
             

def status():
    return isServiceRunning(pidFile)
