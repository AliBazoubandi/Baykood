#!/bin/sh
set -o errexit

python manage.py collectstatic --noinput
python manage.py migrate