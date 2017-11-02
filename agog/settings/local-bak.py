import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
ALLOWED_HOSTS = []

#Uploadcare
UPLOADCARE = {
    'pub_key': '23dbcb6f2d922f1e5edd',
    'secret': '4d98258a66796e954e14',
    'widget_version': '3.2.0',
}