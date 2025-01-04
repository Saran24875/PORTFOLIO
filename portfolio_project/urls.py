# urls.py

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saran112141.pythonanywhere.com.urls')),  # Includes portfolio app's URL patterns
]