"""
archivo principal de url
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    # #urls para aplicacion home
    re_path(r'^', include('applications.home.urls')),
    re_path(r'^', include('applications.biblioteca.urls')),
    re_path('admin/', admin.site.urls),
]
