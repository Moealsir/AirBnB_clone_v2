#!/usr/bin/python3
"""a module that generates a .tgz archives from the web_statics folder"""
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgs archive from the contents of the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        archive_file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive_file))
        return archive_file
    except Exception as e:
        return None
