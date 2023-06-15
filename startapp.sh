#!/bin/bash
set -e

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

uwsgi --ini cv_uwsgi.ini