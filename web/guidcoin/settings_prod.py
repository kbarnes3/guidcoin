from settings_base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'guidcoin_prod',                    # Or path to database file if using sqlite3.
#        'USER': 'guidcoin_prod_user',
#        'PASSWORD': 'passwordgoeshere',
#        'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#        'PORT': '',                      # Set to empty string for default.
#    }
#}

ALLOWED_HOSTS = ['guidcoin.com']

STATIC_ROOT = '/var/www/guidcoin-prod/static'

