# -*- coding: utf-8 -*-
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    shelltools.system("ar x dbeaver-ce-latest-linux-x86_64.deb")
    shelltools.system("tar -xzf data.tar.gz")
    
    pisitools.insinto("/usr/share/dbeaver-ce/", "usr/share/dbeaver-ce/*")
    pisitools.insinto("/usr/share/applications/", "usr/share/applications/dbeaver-ce.desktop")
    pisitools.insinto("/usr/share/metainfo/", "usr/share/metainfo/dbeaver-ce.appdata.xml")
    shelltools.chmod("usr/share/dbeaver-ce/dbeaver", 0o755)
    pisitools.dosym("/usr/share/dbeaver-ce/dbeaver", "/usr/bin/dbeaver")
