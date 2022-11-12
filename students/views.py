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


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    field_list = [
        'Student Name', 'Roll No', 'Class', 'Reg Date', 'Date of birth'
    ]

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Student'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'View Students Info'
        context['field_list'] = self.field_list
        return context


        

