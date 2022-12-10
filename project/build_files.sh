#!/bin/bash

# Used by Vercel to build the application and deploy.
echo "BUILDING THE PROJECT"
python -m pip install -r requirements.txt

echo "MAKING MIGRATIONS"
# python3.6 manage.py makemigrations --noinput
# python3.6 manage.py migrate --noinput

echo "COLLECT STATIC"
python manage.py collectstatic

echo "BUILD END"