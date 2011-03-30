# Django settings for xbrl project.
from private_settings import *
import os, sys

CURRENT_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CURRENT_PATH, 'apps'))

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
    ('comp', os.path.join(CURRENT_PATH, 'static/comp')),
    ('SlickGrid', os.path.join(CURRENT_PATH, 'static/SlickGrid')),
    ('css', os.path.join(CURRENT_PATH, 'static/css')),
    ('js', os.path.join(CURRENT_PATH, 'static/js')),
    ('images', os.path.join(CURRENT_PATH, 'static/images')),
)
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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
    'compilation',
    'debug_toolbar',
)

#For compilation
COMPILER_ROOT = os.path.join(CURRENT_PATH, 'static/comp')

#For django debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    #'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    #'djdt_profile.djdt_profile.ProfilingPanel',
)