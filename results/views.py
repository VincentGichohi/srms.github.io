from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from results.models import DeclareResult
from results.forms import DeclareResultForm
from subjects.models import SubjectCombination
from student_classes.models import StudentClass
from students.models import Student
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json


