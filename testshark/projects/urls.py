"""
This file contains all the routes to the Project app
"""

from django.urls import path
from .views import (
    project_create_view,
    project_detail,
    project_list,
    project_update_view,
    project_delete_view,
)

# URL Patterns for projects app
urlpatterns = [
    path('projects/create/', project_create_view, name='project_create'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('projects/', project_list, name='project_list'),
    path('projects/<int:pk>/update/', project_update_view, name='project_update'),
    path('projects/<int:pk>/delete/', project_delete_view, name='project_delete'),
]