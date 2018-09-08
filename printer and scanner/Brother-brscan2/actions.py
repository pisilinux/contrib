#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import pisitools, shelltools, get


def install():
     
    pisitools.dosym("/usr/local/Brother/sane/brsaneconfig2","/usr/bin/brsaneconfig2")
        
    pisitools.dosym("/usr/lib/libbrcolm2.so.1","/usr/lib/libbrcolm2.so")
        
    pisitools.dosym("/usr/lib/libbrcolm2.so.1.0.1","/usr/lib/libbrcolm2.so.1")
        
    pisitools.dosym("/usr/lib/libbrscandec2.so.1","/usr/lib/libbrscandec2.so")
        
    pisitools.dosym("/usr/lib/libbrscandec2.so.1.0.0","/usr/lib/libbrscandec2.so.1")
        
    pisitools.dosym("/usr/lib/sane/libsane-brother2.so.1","/usr/lib/sane/libsane-brother2.so")
        
    pisitools.dosym("/usr/lib/sane/libsane-brother2.so.1.0.7","/usr/lib/sane/libsane-brother2.so.1")
