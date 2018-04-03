from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View
from groups.models import Group
from students.models import Student, Certificate
from django.db.models.query import QuerySet
from django.db.models import Avg


def all_students(request):
    return HttpResponse(render(request, 'all_students.html', {'students': Student.objects.all()}))


# class-based view
class AddGroupView(View):
    def get(self, request):
        return HttpResponse(render(request, 'add-student.html',
                                   {'groups': Group.objects.all(), 'students': Student.objects.all()}))

    def post(self, request):

        if request.POST.get('name') != None:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            group_id = request.POST.get('group')
            group = Group.objects.get(id=group_id)
            student = Student()

            student.name = name
            student.surname = surname
            student.group = group
            student.save()

            return redirect('/students/all')

        if request.POST.get('subject') != None:
            student = request.POST.get('Student')
            date = request.POST.get('date')
            subject = request.POST.get('subject')
            grade = request.POST.get('grade')
            student_id = request.POST.get('student')
            student = Student.objects.get(id=student_id)
            certificate = Certificate()

            certificate.student = student
            certificate.grade = grade
            certificate.date = date
            certificate.subject = subject
            certificate.save()

            return redirect('/students/all')

        if request.POST.get('namefind') != None:
            students = Certificate.objects.values('student') \
                .annotate(avg_students=Avg('grade')) \
                .order_by('avg_students')
        else:
            students = Certificate.objects.none()

        context = {
            'groups': Group.objects.all(),
            'students': Student.objects.all(),
            'studentsFind': Student.objects.filter(
                name__istartswith=request.POST.get('namefind')
            )
        }

        return HttpResponse(render(request, 'add-student.html', context))


class AddCertificateView(View):
    def post(self, request, student_id):
        try:
            params = dict()

            params['subject'] = request.POST.get('subject')
            params['grade'] = request.POST.get('grade')
            params['student'] = Student.objects.get(id=student_id)

            print(params)
            Certificate.objects.create(**params)
        except Exception as e:
            raise(e)

        return HttpResponse()
