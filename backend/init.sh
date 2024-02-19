source venv/scripts/activate
pip install -r requirements.txt
cd userApi
python manage.py makemigrations
python manage.py migrate
python manage.py runserver