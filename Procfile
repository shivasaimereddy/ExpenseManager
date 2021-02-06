release: pip install django --no-input
release: pip install djangorestframework --no-input
release: pip install django-rest-knox --no-input
release: pip install django-rest-passwordreset --no-input
release: pip install django-cors-headers --no-input
release: pip install django_heroku --no-input
release: pip install gunicorn --no-input
release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn expensemanager.wsgi
