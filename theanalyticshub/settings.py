"""
Django settings for theanalyticshub project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import environ
import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
import sys
import dj_database_url
import logging

root = environ.Path(__file__) - 2
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env()
SITE_ROOT = root()
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# reading .env file
environ.Env.read_env()

# False if not in os.environ
# DEBUG = env('DEBUG')
DEBUG = os.getenv("DEBUG", "False") == "True"

# Setting the Development Mode
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY') # normal syntax from djangoenvirons
SECRET_KEY = os.getenv("SECRET_KEY", 'SAMPLE KEY') # the function needed for deployment


ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "206.189.31.104, ezekiel.206.189.31.104,analyticshub.tech,68.183.71.69,www.analyticshub.tech,ezekiel.analyticshub.tech,127.0.0.1,localhost,ezekiel.localhost").split(",")

# cuustomer user model
AUTH_USER_MODEL = 'account.CustomUser'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'django_hosts',
    'ckeditor',
    'ckeditor_uploader', # Required for using widget with file upload 

    # custom apps
    'mainWebsite',
    'account',
    'professionals',
]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django_hosts.middleware.HostsResponseMiddleware',
]

ROOT_URLCONF = 'theanalyticshub.urls'
ROOT_HOSTCONF = 'theanalyticshub.hosts'
DEFAULT_HOST = ' '
PARENT_HOST = 'localhost:8000'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/ 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'theanalyticshub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# DATABASES = {
#     'default': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db'),
#     # read os.environ['SQLITE_URL']
#     'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
# }

'''
facilitate development of application locally - determine
if DEVELOPMENT_MODE is set to True and which database should be accessed

Django shouldn't attempt to make a database connection to the 
PostgreSQL database when attempting to collect the static files

so examine the command that was executed and not connect to a database 
if the command given was collectstatic.

 App Platform will automatically collect static files when the app is deployed.
 '''
if DEVELOPMENT_MODE is True:
    DATABASES = {
        'default': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db'),
        # read os.environ['SQLITE_URL']
        'extra': env.db('SQLITE_URL', default='sqlite:////tmp/my-tmp-sqlite.db')
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    #if os.getenv("DATABASE_URL", None) is None:
     #   pass
        #raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": {
            # 'ENGINE':'django.db.backends.postgresql_psycopg2',
            'ENGINE':'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRESS_NAME', None),
            'USER': os.getenv('POSTGRESS_USER', None),
            'PASSWORD': os.getenv('POSTGRESS_PSSWRD', None),
            'HOST': '',
            'PORT': ''
	},
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
public_root = root.path('public/')
MEDIA_ROOT = public_root('media')
MEDIA_URL = env.str('MEDIA_URL', default='/media/')

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = env.str('STATIC_URL', default='/static/')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "public"),
    os.path.join(BASE_DIR, "favicon"),
]

# ref:https://github.com/django-compressor/django-compressor/issues/720
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',    #causes verbose duplicate notifications in django 1.9
# )

# This setting specifies a relative path to your CKEditor media upload directory.
# CKEditor uses Django’s storage API. By default,
# Django uses the file system storage backend
# (it will use your MEDIA_ROOT and MEDIA_URL) 
# and if you don’t use a different backend you have to have 
# write permissions for the CKEDITOR_UPLOAD_PATH path within MEDIA_ROOT
CKEDITOR_UPLOAD_PATH = "image_uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_FORCE_JPEG_COMPRESSION=True
# Whitenoise: Add compression and caching support
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# If a file isn’t found in the staticfiles.json manifest at runtime, a ValueError is raised
# This disables that behaviour
WHITENOISE_MANIFEST_STRICT = False

# related to errors in terminal
# refer: https://github.com/wagtail/wagtail/issues/4254
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

# Having server 500 errors
# refer: https://stackoverflow.com/questions/52311724/500-error-when-debug-false-with-heroku-and-django

# This helps me see errors when debug set to false
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True
