"""
WSGI config for carshop_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import dotenv
from whitenoise.django import DjangoWhiteNoise


from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv(os.path.join(os.path.dirname(__file__), 'settings', '.env'))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.deploy")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

