#!/usr/bin/python3
""" Compress before sending """
from fabric.api import *
from os.path import getsize
import os


env.hosts = ['35.243.187.246', '3.85.202.216']


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
