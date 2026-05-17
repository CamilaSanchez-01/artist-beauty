"""
WSGI config for artist_beauty project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artist_beauty.settings')
application = get_wsgi_application()
