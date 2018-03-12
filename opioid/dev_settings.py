import os
from .base_settings import *
import os

secret_file = open(os.path.join(os.path.dirname(__file__), 'secret_keys.json'), 'r').read()
SECRETS = json.loads(secret_file)
# Dev Environment specific settings
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES['default']['NAME'] = 'opioid_db'

# Django debug toolbar settings
INSTALLED_APPS += ['debug_toolbar']

# Staticfiles settings
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INTERNAL_IPS = ('::ffff:10.0.2.2',)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

MIDDLEWARE = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE


# Development URLs
ROOT_URLCONF = 'opioid.dev_urls'

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ['rest_framework.permissions.AllowAny']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'watched_file': {
            'level': 'INFO',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/opioid.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['watched_file', ],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
