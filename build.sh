#!/usr/bin/env bash
set -o errexit  # stop on error

pip install -r requirements.txt

python manage.py migrate --noinput
python manage.py tailwind build
python manage.py collectstatic --noinput --clear
