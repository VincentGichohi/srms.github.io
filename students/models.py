from django.db import models
from student_classes.models import StudentClass
from django.urls import reverse
from datetime import date


class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    student_name = models.CharField(max_length=100)
    student_roll = models.IntegerField(unique=True)
    student_email = models.EmailField()
    student_gender = models.CharField(max_length=8, choices=GENDER)
    student_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    student_date_of_birth = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('students:student_create')

    def __str__(self):
        return self.student_name
