from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.report_view, name='report_view'),
]