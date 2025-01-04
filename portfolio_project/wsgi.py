# wsgi.py

import os
from django.core.wsgi import get_wsgi_application # type: ignore

# Set the default settings module for the 'wsgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()