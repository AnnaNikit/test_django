from django.contrib import admin
from django.urls import path, re_path
from students.views import all_students, AddGroupView


urlpatterns = [
    path('all', all_students),
    path('add', AddGroupView.as_view()),
    path('findstudent', AddGroupView.as_view()),
]
