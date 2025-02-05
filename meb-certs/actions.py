#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("openssl x509 -inform DER -outform PEM -in MEB_SERTIFIKASI.cer -out MEB_SERTIFIKASI.crt")

def install():
    pisitools.insinto("/usr/share/ca-certificates/", "MEB_SERTIFIKASI.crt")
