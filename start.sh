#!/bin/bash

cd backend

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the Django server
python manage.py runserver 0.0.0.0:$PORT
