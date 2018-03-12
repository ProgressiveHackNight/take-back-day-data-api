import os
from .base_settings import *

secret_file = open(os.path.join(os.path.dirname(__file__), 'secret_keys.json'), 'r').read()

SECRETS = json.loads(secret_file)
# Django Environment Specific Settings
DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES['default']['NAME'] = 'opioid_db'

# Static files
STATIC_ROOT = '/srv/static/'
MEDIA_ROOT = '/srv/media/'

# Development URLs
ROOT_URLCONF = 'opioid.production_urls'

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ['rest_framework.permissions.IsAuthenticated']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'watched_file': {
            'level': 'INFO',
            'class':'logging.handlers.WatchedFileHandler',
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
