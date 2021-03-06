# Django settings for Votrasi project.
import os

from custom_settings import *

ADMINS = (
    ('Ramsey', 'ramsey@pixelcode.ca'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'


LANGUAGE_CODE = 'en-us'

SITE_ID = 1


USE_I18N = True


USE_L10N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

MEDIA_URL = '/media/'


STATIC_ROOT = ''

STATIC_URL = '/static/'


ADMIN_MEDIA_PREFIX = '/admin_media/'
ADMIN_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..' , 'parts', 'django', 'django', 'contrib', 'admin', 'media')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_0g6i!3@h_y5^6viee%$homc7ms0zg$6_s1njo0=03_d*!q4rq'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pixelcode.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates')
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
     'pixelcode',
     'filebrowser',
     'pixelcode.blog',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "pixelcode.context_processors.main",
    "pixelcode.context_processors.latest_tweet",
)

TWITTER_USER = "pixel_code"
TWITTER_TIMEOUT = 3600

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER = False

FILEBROWSER_URL_FILEBROWSER_MEDIA = '/media/filebrowser/'