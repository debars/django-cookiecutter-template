# Production & Deployment settings

from .base import *

PRODUCTION = True

SECRET_KEY = '{{ secret_key }}'

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'password',
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'HOST': 'localhost',
        # Empty string for default
        'PORT': '',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['public/templates'],
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

# Static and media files should exist seperate in development
# set your static root in production.py

STATIC_URL = '/static/'

STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public/components'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media')
