#!/usr/bin/python3
""" Compress before sending """
from fabric.api import *
from datetime import datetime


def do_pack():
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    path_file = local(
        "tar -cvzf versions/web_static_{}.tgz web_static".format(time))
    if path_file.succeeded:
        return('versions/web_static_{}.tgz'.format(time))
    else:
        return False
