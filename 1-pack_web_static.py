#!/usr/bin/python3
"""a module that generates a .tgz archives from the web_statics folder"""
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgs archive from the contents of the web_static folder"""
    date = datetime.utcnow()
    archive_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                                 date.month,
                                                                 date.day,
                                                                 date.hour,
                                                                 date.minute,
                                                                 date.second)

    if os.path.isdir("versions") is not True:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_statics".format(archive_file)).failed is True:
        return None
    return archive_file
