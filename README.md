# L_Center
Learning Centre website

## Dars ketma-ketligi
```shell
virtualenv venv
source venv/bin/activate
pip install django pillow
mkdir media
mkdir static
mkdir templates
django-admin startproject config .
django-admin startapp course
django-admin startapp contact
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```