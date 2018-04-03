from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    max_students = models.IntegerField()

    def __repr__(self):
        return f'<Group(' \
               f'name={self.name}, ' \
               f'start_date={self.start_date}, ' \
               f'max_students={self.max_students}' \
               f')>'
