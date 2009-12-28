# Django settings for shopjet project.
import os
import local_settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DOC_ROOT = os.path.dirname(__file__)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = local_settings.DATABASE_ENGINE
DATABASE_NAME   = local_settings.DATABASE_NAME
DATABASE_USER   = local_settings.DATABASE_USER
DATABASE_PASSWORD = local_settings.DATABASE_PASSWORD
DATABASE_HOST   = local_settings.DATABASE_HOST
DATABASE_PORT   = local_settings.DATABASE_PORT

EMAIL_HOST      = local_settings.EMAIL_HOST
EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = local_settings.DEFAULT_FROM_EMAIL
SERVER_EMAIL    = local_settings.SERVER_EMAIL

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'he'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

ugettext = lambda s: s

LANGUAGES = (
    ('he', ugettext('Hebrew')),
    ('en', ugettext('English')),
)


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
import os
basedir = os.path.dirname(globals()["__file__"])
STATIC_SUFFIX = 'static'
MEDIA_ROOT = os.path.abspath(os.path.join(basedir, STATIC_SUFFIX))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/%s/' % STATIC_SUFFIX

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'rg%g*3nuh(jxdvpc+@%cm1@xt_nnmc8w3+0cukpo2bb8jp_eq0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'shopjet.urls'

set_dir = lambda x: os.path.join(DOC_ROOT, x).replace('\\','/')
TEMPLATE_DIRS = [
    set_dir("templates"),
    set_dir("coupon\\templates"),
    set_dir("people\\templates"),
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'shopjet.my_db'
    
)
