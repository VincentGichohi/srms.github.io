from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

