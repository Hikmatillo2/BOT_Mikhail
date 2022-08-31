#!/bin/bash

service nginx start
service postgresql start
python3 manage.py migrate --fake sessions zero
python3 manage.py migrate --fake-initial
python3 manage.py migrate
python3 manage.py initadmin
/bin/gunicorn3 wsgi:application -b 127.0.0.1:8000 --env DJANGO_SETTINGS_MODULE=settings.development --user www-data --group www-data
