# Technical

- Postgres running in docker container
  + $ docker run -d --name my_postgres -v my_dbdata:/var/lib/postgresql/data -p 54320:5432 postgres:11
  + import database backup 
  + Start PGAdmin app:  http://127.0.0.1:50533/browser/

- Django
  + Auth, Admin
  + https://github.com/ctxis/django-admin-view-permission
  + 
  
# Quick Note

- learn about class Meta?

- Terminal
  + $ python manage.py makemigrations

  + $ python manage.py migrate

  + $ python manage.py runserver
