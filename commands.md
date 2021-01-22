py -m venv venv
.\venv\Scripts\activate
pip install django
python-admin startproject core .
py manage.py migrate
py manage.py makemigrations
py manage.py createsuperuser
python manage.py runserver
ctrl-c - close-server
ctrl-l - clear terminal
pip freeze > requirements.txt
py manage.py test
pip install django-coverage