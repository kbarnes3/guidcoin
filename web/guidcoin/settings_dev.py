from settings_base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'guidcoin_dev',                        # Or path to database file if using sqlite3.
        'USER': 'guidcoin_dev_user',
        'PASSWORD': 'passwordgoeshere',
        'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

STATIC_ROOT = '/var/www/guidcoin-dev/static'

