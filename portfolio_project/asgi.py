# asgi.py

import os
from django.core.asgi import get_asgi_application # type: ignore

# Set the default settings module for the 'asgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_asgi_application()