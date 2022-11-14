from django.db import models
from students.models import Student
from subjects.models import StudentClass
from django.urls import reverse
from django.contrib.postgres.fields import JSONField


class DeclareResult(models.Model):
    select_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    select_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = JSONField(blank=True)

    def get_absolute_url(self):
        return reverse('results:declare_result')

    def __str__(self):
        return "%s Section-%s" % (self.sele~ct_class.class_name, self.select_class.section)