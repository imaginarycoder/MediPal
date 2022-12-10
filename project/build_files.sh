# Used by Vercel to build the application and deploy.
echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
echo  "BUILD END"