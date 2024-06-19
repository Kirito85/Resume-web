from django.core.wsgi import get_wsgi_application
from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = get_wsgi_application()
