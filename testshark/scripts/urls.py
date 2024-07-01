from django.urls import path
from . import views

# URL Patterns for scripts app
urlpatterns = [
    path('testcases/<int:pk>/generate_script/', generate_script_view, name='generate_script'),
    path('scripts/<int:pk>/', script_detail, name='script_detail'),
]