#!/usr/bin/python3
""" Compress before sending """
from fabric.api import *
from datetime import datetime
from os.path import getsize
import os


env.hosts = ['35.243.187.246', '3.85.202.216']


@task
def deploy():
    path_file = do_pack()
    if os.path.isfile(path_file):
        val = do_deploy(path_file)
        return val
    else:
        return False


def do_pack():
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    path_file = local(
        "tar -cvzf versions/web_static_{}.tgz web_static".format(time))
    size = getsize("versions/web_static_{}.tgz".format(time))
    if path_file.succeeded:
        print("web_static packed: versions/web_static_{}.tgz ->\
 {}Bytes".format(time, size))
        return('versions/web_static_{}.tgz'.format(time))
    else:
        return None


def do_deploy(archive_path):
    if os.path.isfile(archive_path):
        split1 = archive_path.split("/")
        split2 = archive_path.split(".")
        n_file = split2[0]
        archive = split1[-1]
        put(archive_path, "/tmp/")
        sudo('mkdir -p /data/web_static/releases/{}'.format(n_file))
        sudo('tar -xzf /tmp/{} -C /data/web_static\
/releases/{}'.format(archive, n_file))
        sudo('rm /tmp/{}'.format(archive))
        sudo('mv /data/web_static/releases/{}/web_static/* /data/web_static\
/releases/{}'.format(n_file, n_file))
        sudo('rm -rf /data/web_static/releases/{}/web_static'.format(n_file))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases/{}/ /data/web_static\
/current'.format(n_file))
        print('New version deployed!')
        return True
    else:
        return None
