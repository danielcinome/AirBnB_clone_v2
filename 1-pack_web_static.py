#!/usr/bin/python3
""" Compress before sending """
from fabric.api import *
from datetime import datetime
from os.path import getsize


def do_pack():
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    path_file = local(
        "tar -cvzf versions/web_static_{}.tgz ./web_static".format(time))
    size = getsize("versions/web_static_{}.tgz".format(time))
    if path_file.succeeded:
        print("web_static packed: versions/web_static_{}.tgz ->\
 {}Bytes".format(time, size))
        return('versions/web_static_{}.tgz'.format(time))
    else:
        return None
