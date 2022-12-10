from django.shortcuts import render, redirect, get_object_or_404
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
# from results.models import DeclareResult
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core import serializers
import json

from student_classes.models import StudentClass
from results.models import DeclareResult
from subjects.models import Subject
from students.models import Student


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("\nUser Name = ", username)
        print("Password = ", password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            context = {'message': 'Invalid User Name and Password'}
            return render(request, 'index.html', context)
    return render(request, 'index.html', {'name': 'Vincent Gichohi', 'pass': 'demo@srms'})

        
