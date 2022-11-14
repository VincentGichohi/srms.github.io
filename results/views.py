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


def validated_data(request):
    smt = SubjectCombination.objects.all()
    data = {}
    if request.method == 'GET':
        rc = request.GET['selectedClass']
        subjects = []
        for s in smt:
            if s.select_class.class_name in rc and s.select_class.section in rc:
                subjects.append(s.select_subject)
        sir_subjects = serializers.serialize('json', subjects)
        data['subjects'] = sir_subjects
        return JsonResponse(data)
    subjects = None
    data['result'] = 'Your made a request with empty data'
    return HttpResponse(json.dumps(data), content_type="application/json")


