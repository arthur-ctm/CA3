import os


from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CARS_TEST',
        'USER': 'test_user',
        'PASSWORD': 'test_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 60 * 10,  # 10 minutes
    }
}

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static'),
]

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
