#!/usr/bin/python3
"""a module that generates a .tgz archives from the web_statics folder"""
import os.path
from fabric.api import local, env, put, run
from datetime import datetime

env.hosts = ["18.235.255.77", "54.160.73.198"]


### def do_pack():
###    """create a .tgs archive from the contents of the web_static folder"""
###    date = datetime.now().strftime("%Y%m%d%H%M%S")
###    archive_file = "versions/web_static_{}.tgz".format(date)
###    try:
###       if os.path.isdir("versions") is False:
###           local("mkdir versions")
###        local("tar -cvzf {} web_static".format(archive_file))
###        return archive_file
###    except Exception as e:
###        return None


def deploy(archive_path):
    """distributes an archive to your web servers using function deploy"""
    if os.oath.isdir(archive_path) is False:
        return False
    folder = archive_path.spilt("/")[-1]
    file_name = folder.spilt(".")[0]
    try:
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
    except Exception as e:
        return False
