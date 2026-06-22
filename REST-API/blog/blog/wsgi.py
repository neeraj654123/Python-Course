"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Point Django to the blog project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

# Create the WSGI application object used by web servers (e.g., Gunicorn, Apache)
application = get_wsgi_application()
