from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import StudentClass
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms



class StudentClassCreateView(LoginRequiredMixin, CreateView):
    model = StudentClass
    form_class = forms.StudentClassForm

    

