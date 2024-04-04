#!/usr/bin/python3
"""a module that istributes an archive to your web servers, 
using the function do_deploy
"""
import os.path
from fabric.api import env, put, run
env.hosts = ["18.235.255.77", "54.160.73.198"]


def do_deploy(archive_path):
    """distributes an archive to your web servers using function deploy"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        folder = archive_path.spilt("/")[-1]
        file_name = folder.spilt(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(folder, path, file_name))
        run('rm /tmp/{}'.format(folder))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_name))
        run('rm -rf {}{}/web_static'.format(path, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_name))
        return True
    except:
        return False
