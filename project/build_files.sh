# Used by Vercel to build the application and deploy.
echo "BUILD START"
python3.6 -m pip install -r requirements.txt
python3.6 manage.py collectstatic --noinput --clear
echo  "BUILD END"