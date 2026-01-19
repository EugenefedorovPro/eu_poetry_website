#!/bin/sh


python manage.py makemigrations 
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn eu_website_project.wsgi:application --bind 0.0.0.0:8008 --timeout 600
