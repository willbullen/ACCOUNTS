from .settings import *
import os

# Production settings
DEBUG = False

# Security settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'djangoledger1234!DoNotUse!BadIdea!VeryInsecure!')
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.manusvm.computer', 'https://*.railway.app', 'https://*.fly.dev']

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Database - keep SQLite for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
