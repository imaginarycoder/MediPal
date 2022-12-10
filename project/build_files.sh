#!/bin/bash

# Used by Vercel to build the application and deploy.
echo "BUILDING THE PROJECT"
python3.6.8 -m pip install -r requirements.txt

echo "MAKING MIGRATIONS"
# python3.6 manage.py makemigrations --noinput
# python3.6 manage.py migrate --noinput

echo "COLLECT STATIC"
python3.6.8 manage.py collectstatic --noinput --clear

echo "BUILD END"