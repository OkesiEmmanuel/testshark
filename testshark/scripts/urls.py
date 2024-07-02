from django.urls import path
from . import views

# URL Patterns for scripts app
urlpatterns = [
    path('testcases/<int:pk>/generate_script/', views.generate_script_view, name='generate_script'),
    path('scripts/<int:pk>/', views.script_detail, name='script_detail'),
]