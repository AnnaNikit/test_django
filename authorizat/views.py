from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpRequest
from django.views import View
from groups.models import Group
from students.models import Student, Certificate
from django.db.models.query import QuerySet
from django.db.models import Avg
from django.contrib import auth
from django.contrib.auth import authenticate, login



def authorizat(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'auth.html'))
    elif request.method == 'POST':

        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('zzzzzzzzzzzzzzzzzzzz')
            return HttpResponse('ok')
        else:
            print('z')
            return HttpResponse('ok')
