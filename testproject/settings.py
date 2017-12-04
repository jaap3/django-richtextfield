import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '--1oh7*5-1_rr%*34^&@e^b59(vgv=zm1wt(wm1ga=pfm73(9i'

DEBUG = True
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

STATIC_URL = '/static/'

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
