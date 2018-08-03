from .base import *


DEBUG = True

ALLOWED_HOSTS = ['denissvistunov.pythonanywhere.com', '*']

MEDIA_URL = '/images/'

SESSION_COOKIE_SECURE = True

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'