from django.db import models
from django.urls import reverse


class StudentClass(models.Model):
    class_name = models.CharField(max_length=100, help_text='Eg- Third, Fourth, Sixth etc')
    class_name_in_numeric = models.IntegerField(help_text='E.g 1,2,3,4,5 etc')
    section = models.CharField(max_length=10, help_text='Eg A, B, C etc')
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('student_classes:class_list')

    def __str__(self):
        return "%s Section-%s"%(self.class_name, self.section)
        