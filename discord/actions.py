#!/usr/bin/python
# Created For PisiLinux
from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = ["/"]


def setup():
    pisitools.dosed('Discord/discord.desktop', 'Exec=.*', 'Exec=/usr/bin/discord')


def install():
    pisitools.insinto("/opt/discord/", "Discord/*")
    pisitools.dosym('/opt/discord/Discord', '/usr/bin/discord')
    pisitools.dosym('/opt/discord/discord.png', '/usr/share/pixmaps/discord.png')
    pisitools.dosym('/opt/discord/discord.desktop', '/usr/share/applications/discord.desktop')

    pisitools.remove('/opt/discord/postinst.sh')
    pisitools.remove('/opt/discord/libEGL.so')
    pisitools.remove('/opt/discord/swiftshader/libEGL.so')
    pisitools.remove('/opt/discord/libGLESv2.so')
    pisitools.remove('/opt/discord/swiftshader/libGLESv2.so')

    pisitools.dosym('/usr/lib/libEGL.so', '/opt/discord/libEGL.so')
    pisitools.dosym('/usr/lib/libEGL.so', '/opt/discord/swiftshader/libEGL.so')
    pisitools.dosym('/usr/lib/libGLESv2.so', '/opt/discord/libGLESv2.so')
    pisitools.dosym('/usr/lib/libGLESv2.so', '/opt/discord/swiftshader/libGLESv2.so')

    pisitools.dodoc('LICENSE.html', 'OSS-LICENSES.html')
