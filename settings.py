# Django settings for xbrl project.
from private_settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ('admin', '/home/zeebo/Code/envs/xbrldjango/lib/python2.6/site-packages/django/contrib/admin/media/'),
)
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'xbrldjango.urls'

TEMPLATE_DIRS = (
    'templates',
)

SPHINX_API_VERSION = 0x116

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'south',
    'djangosphinx',
    'xbrldjango.taxonomy',
    'compilation',
)

COMPILER_ROOT = ''
