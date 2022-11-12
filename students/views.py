from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectCombination
from .forms import SubjectForm, SubjectCombinationForm
from django.urls import reverse_lazy


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm

    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Creation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Add Subject'
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


class StudentUpdateVIew(LoginRequiredMixin, UpdateView):
    model = Student
    template_name_suffix = '_form'
    form_class = StudentForm
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateVIew, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Update Student Info'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Update Student Info'
        return context



class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name_suffix = '_delete'
    success_url = reverse_lazy('students:student_list')

    def get_context_data(self, **kwargs):
        context =  super(StudentDeleteView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Student Delete Confirmation'
        context['panel_name'] = 'Students'
        context['panel_title'] = 'Delete Student'
        return context





