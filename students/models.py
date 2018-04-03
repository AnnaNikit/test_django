from django.db import models
from groups.models import Group

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False)

class Certificate(models.Model):
    subject = models.CharField(max_length=255, null=False, blank=False)
    grade   = models.IntegerField()
    date   = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
