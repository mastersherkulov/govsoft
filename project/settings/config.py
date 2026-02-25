import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DEBUG TOOLBAR
INTERNAL_IPS = [
    "127.0.0.1",
]
# END DEBUG TOOLBAR

# ALLOWED HOSTS
ALLOWED_HOSTS = ['*']
# END ALLOWED HOSTS

# CORS
CORS_ALLOW_METHODS = ['*']
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# END CORS

# DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": __import__('datetime').timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": __import__('datetime').timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": os.environ.get('SECRET_KEY'),
}
