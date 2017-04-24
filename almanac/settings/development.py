from .common import *

# TOTALLY INSECURE: We only hard-code the SECRET_KEY in development
SECRET_KEY = 'insecure-development-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
