"""
Django settings for testproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--1oh7*5-1_rr%*34^&@e^b59(vgv=zm1wt(wm1ga=pfm73(9i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djrichtextfield',
    'testproject.testapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


# Use discover_runner for Django < 1.6
try:
    from django.test.runner import DiscoverRunner  # noqa
except ImportError:
    TEST_RUNNER = 'discover_runner.DiscoverRunner'


# Django Rich Text Field
TINYMCE_CONFIG = {
    'js': ['//tinymce.cachefly.net/4.1/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image table code',
        'toolbar': 'formatselect | bold italic | removeformat |'
                   ' link unlink image table | code',
        'block_formats': 'Paragraph=p;Header 1=h1;Header 2=h2;Header 3=h3',
        'width': 700
    },
    'profiles': {
        'mini': {
            'toolbar': 'bold italic | removeformat'
        }
    }
}

CKEDITOR_CONFIG = {
    'js': ['//cdn.ckeditor.com/4.4.4/standard/ckeditor.js'],
    'init_template': 'djrichtextfield/init/ckeditor.js',
    'settings': {
        'toolbar': [
            {'items': ['Format', '-', 'Bold', 'Italic', '-', 'RemoveFormat']},
            {'items': ['Link', 'Unlink', 'Image', 'Table']},
            {'items': ['Source']}
        ],
        'format_tags': 'p;h1;h2;h3',
        'width': 700,
    },
    'profiles': {
        'mini': {
            'toolbar': [
                {'items': ['Bold', 'Italic', '-', 'RemoveFormat']},
            ]
        }
    }
}

DJRICHTEXTFIELD_CONFIG = CKEDITOR_CONFIG
