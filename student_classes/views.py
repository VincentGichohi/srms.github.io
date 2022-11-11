from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import StudentClass
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms



class StudentClassCreateView(LoginRequiredMixin, CreateView):
    model = StudentClass
    form_class = forms.StudentClassForm

    def get_context_data(self, **kwargs):
        context = super(StudentClassCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Add Student Class'
        context['panel_name'] = 'Classes'
        context['panel_title'] = 'Add Class'
        return context


class StudentClassListView(LoginRequiredMixin, ListView):
    mode = StudentClass



