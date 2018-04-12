from django.contrib import admin
from django.urls import path, re_path
from groups.views import all_groups, AddGroupView, add_group
from authorizat.views import authorizat
authorizat

urlpatterns = [
    path('all', all_groups),
    path('add', AddGroupView.as_view()),
    path('/authorizat/login', authorizat),
]
