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


def declare_result_view(request):
    context = {}
    if request.method == 'POST':
        form = request.POST
        data = json.loads(json.dumps(form))
        data.pop('csrfmiddlewaretoken')
        pk = data['select_class']
        student = Student.objects.get(id=pk)
        data.pop('select_class')
        data.pop('select_student')
        DeclareResult.objects.create(select_class=clas, select_student=student, marks=data)
    else:
        form = DeclareResultForm()
        context['main_page_title'] = 'Declare Students Result'
        context['panel_name'] = 'Results'
        context['panel_title'] = 'Declare Result'
        context['form'] = form
    return render(request, 'results/declareresult_form.html', context)


def setup_update_view(request):
    data = {}
    if request.method == 'GET':
        pk_value = int(request.GET['pk_value'])
        result_obj = get_object_or_404(DeclareResult, pk=pk_value)
        dt = result_obj.marks
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')


@login_required
def result_update_view(request, pk):
    result = get_object_or_404(DeclareResult, pk=pk)
    form = DeclareResultForm(instance=result)
    context = {
        'main_page_title': 'Update Students Result',
        'panel_name': 'Results',
        'panel_title': 'Update Result',
        'form': form, 'pk': pk}
    if request.method == 'POST':
        all_data = request.POST
        data = json.loads(json.dumps(all_data))
        data.pop('csrfmiddlewaretoken')
        pk = data['select_class']
        clas = StudentClass.objets.get(id=pk)
        pk = data['select_student']
        student = Student.objects.get(id=pk)
        data.pop('select_class')
        data.pop('select_student')
        print("Modified Data = ", data)
        result.select_class = clas
        result.select_student = student
        result.marks = data
        result.save()
        print('\nResult updated\n')
        return redirect('results:result_list')
    return render(request, 'results/update_form.html', context)



