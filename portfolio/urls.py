# urls.py

from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]