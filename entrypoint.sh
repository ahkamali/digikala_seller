#!/bin/sh

# Apply database migrations
python manage.py migrate
python manage.py makemigrations


# Start the Django server
python manage.py runserver 0.0.0.0:8000
