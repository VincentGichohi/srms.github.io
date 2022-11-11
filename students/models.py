from django.db import models
from student_classes.models import StudentClass
from django.urls import reverse
from datetime import date


class Student(models.Model):
    gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    )
    