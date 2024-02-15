#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers. """

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except:
        return None
