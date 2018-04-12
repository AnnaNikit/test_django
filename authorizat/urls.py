from django.contrib import admin
from django.urls import path, re_path
from authorizat.views import authorizat


urlpatterns = [
    path('login', authorizat),
]
