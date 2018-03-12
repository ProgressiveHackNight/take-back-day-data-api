import os

from .base_settings import *

# Dev Environment specific settings

DEBUG = False
ALLOWED_HOSTS = ['*', 'takebackday.infoloom.com']

# Static Files Settings
STATIC_ROOT = '/srv/static/'
MEDIA_ROOT = '/srv/media/'

# Development URLs
ROOT_URLCONF = 'opioid.production_urls'
