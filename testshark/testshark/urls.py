from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from testshark_tool.views import dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name= 'dashboard'),
    path('users/', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('testcase/', include('testcases.urls')),
    path('scripts/', include('scripts.urls')),
    path('reports/', include('reports.urls')),
    
]