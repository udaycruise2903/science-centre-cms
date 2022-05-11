from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-95!yx5q^97zhq5a&*#l3*20(xeg86+0trsbks-i94+u5^ksw1b'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': os.environ.get("POSTGRES_ENGINE"),
        'NAME': os.environ.get("POSTGRES_DATABASE"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': os.environ.get("POSTGRES_PORT"),
    }
}

try:
    from .local import *
except ImportError:
    pass
