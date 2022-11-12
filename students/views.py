from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    from_class = StudentForm

    def get_context_data(self, **kwargs):
        context =  super(StudentCreateView, self).get_context_data(**kwargs)
        context['amin_page_title'] = 'Student Creation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Create Student'
        return context
        

