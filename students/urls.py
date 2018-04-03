from django.contrib import admin
from django.urls import path, re_path
from students.views import all_students, AddGroupView, AddCertificateView

urlpatterns = [
    path('all', all_students),
    path('add', AddGroupView.as_view()),
    path('findstudent', AddGroupView.as_view()),
    path('<int:student_id>/certificate/add', AddCertificateView.as_view()),
]
