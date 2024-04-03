#!/usr/bin/env bash
# Sets up a web server for deployment of Airbnb_clone_web_static.

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo sed -i '38i\ \ location /hbnb_static/ {\n \ \ \ \ alias /data/web_static/current/;\n \ \ }\n' /etc/nginx/sites-available/default
sudo service nginx start
