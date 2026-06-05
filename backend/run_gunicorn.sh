#!/bin/sh

cd /home/ubuntu/defendid.github.io/backend
. .venv/bin/activate
gunicorn --bind unix://flask.sock app:app
chmod 755 flask.sock
