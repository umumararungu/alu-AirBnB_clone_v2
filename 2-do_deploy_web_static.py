#!/usr/bin/python3
from fabric.api import env, put, run
import re
import os
from os.path import exists, isdir


env.user = "ubuntu"
env.hosts = ["204.236.196.88", "34.224.218.238"]
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """
    Distributes archive to web servers
    """
    if not exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    filename = re.search(r"[^/]+$", archive_path).group(0)
    folder = "/data/web_static/releases/{}".format(
        os.path.splitext(filename)[0])

    if not exists(folder):
        run("mkdir -p {}".format(folder))

    run("tar -xzf /tmp/{} -C {}".format(filename, folder))

    run("rm /tmp/{}".format(filename))

    run("mv {}/web_static/* {}".format(folder, folder))

    run("rm -rf {}/web_static".format(folder))

    run("rm -rf /data/web_static/current")

    run("ln -s {} /data/web_static/current".format(folder))

    if not isdir("/var/www/html/hbnb_static"):
        run("sudo mkdir -p /var/www/html/hbnb_static")

    run("sudo cp -r /data/web_static/current/* /var/www/html/hbnb_static/")

    print("New version deployed!")
    return True
