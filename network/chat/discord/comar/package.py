import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("update-desktop-database")

def postRemove():
    os.system("update-desktop-database")