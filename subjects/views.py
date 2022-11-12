from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Subject, SubjectCombination
from .forms import SubjectForm, SubjectCombinationForm
from django.urls import reverse_lazy


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm

    def get_context_data(self, **kwargs):
        context =  super(SubjectCreateView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Subject Creation'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'Add a subject'
        return context


class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    field_list = [
        'Subject Name', 'Subject Code', 'Creation Date', 'Last Updated'
    ]

    def get_context_data(self, **kwargs):
        context = super(SubjectListView, self).get_context_data(**kwargs)
        context['main_page_title'] = 'Manage Subjects'
        context['panel_name'] = 'Subjects'
        context['panel_title'] = 'View SUbjects Info'
        context['field_list'] = self.field_list
        return context


class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    template_name_suffix = '_form'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:subject_list')


class SubjedctDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    form_class = SubjectCombinationForm
    template_name_suffix = '_delete'

    def get_context_data(self, **kwargs):
        context = super(SubjedctDeleteView, self).get_context_data(**kwargs)
        
