from typing import Dict

from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
import datetime
from django.http import JsonResponse
from django.views.generic import View
from .documents import ProjectDocument

# Create your views here. (KENT)
'''def add_unit(request):
    unit = UnitNumber.objects.all()
    if request.method == 'POST':
        unit_number = UnitNumberForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return redirect('unit_list')
        elif unit_number.is_valid():
            unit_number.save()

    else:
        unit_number = UnitNumberForm()
        project = ProjectForm()
    return render(request, 'object/unit_list.html',
                  {'unit': unit, 'unit_number': unit_number, 'project': project})

def add_phase(request):
    if request.method == 'POST':
        add_phase = PhaseForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
        elif add_phase.is_valid():
            add_phase.save()
            return redirect('phase_list')
    else:
        add_phase = PhaseForm()
        project = ProjectForm()
    return render(request, 'object/phase_list.html',
                  {'phase': phase, 'add_phase': add_phase, 'project': project})

def add_project(request):
    project = Project.objects.all()
    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        if add_project.is_valid():
            add_project.save()
            return redirect('project_list')
    else:
        add_project = ProjectForm()
    return render(request, 'object/project_list.html', {'project': project, 'add_project': add_project})'''

'''def project_main_list(request):
    unit = UnitNumber.objects.all()

    return render(request, 'object/project_main_list.html', {'unit': unit})'''


def unit_list(request):
    unit = UnitNumber.objects.all()
    q = request.GET.get('q')
    if q:
        posts = Pos
    if request.method == 'POST':
        unit_number = UnitNumberForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return redirect('unit_list')
        elif unit_number.is_valid():
            unit_number.save()

    else:
        unit_number = UnitNumberForm()
        project = ProjectForm()
    return render(request, 'object/unit_list.html',
                  {'unit': unit, 'unit_number': unit_number, 'project': project})


def unit_list(request):
    unit = UnitNumber.objects.all()
    if request.method == 'POST':
        unit_number = UnitNumberForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return redirect('unit_list')
        elif unit_number.is_valid():
            unit_number.save()

    else:
        unit_number = UnitNumberForm()
        project = ProjectForm()
    return render(request, 'object/unit_list.html',
                  {'unit': unit, 'unit_number': unit_number, 'project': project})


def project_list(request):
    project = Project.objects.all()
    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        if add_project.is_valid():
            add_project.save()
            return redirect('project_list')
    else:
        add_project = ProjectForm()
    return render(request, 'object/project_list.html', {'project': project, 'add_project': add_project})


def phase_list(request):
    phase = Phase.objects.all()
    if request.method == 'POST':
        add_phase = PhaseForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
        elif add_phase.is_valid():
            add_phase.save()
            return redirect('phase_list')
    else:
        add_phase = PhaseForm()
        project = ProjectForm()
    return render(request, 'object/phase_list.html',
                  {'phase': phase, 'add_phase': add_phase, 'project': project})


def unit_edit(request, id):
    unit = UnitNumber.objects.get(pk=id)
    form = UnitNumberForm(instance=unit)
    if request.method == 'POST':
        form = UnitNumberForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    return render(request, 'object/unit_edit.html', {'form': form})


def project_edit(request, id):
    project = Project.objects.get(pk=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    return render(request, 'object/project_edit.html', {'form': form})


def phase_edit(request, id):
    phase = Phase.objects.get(pk=id)
    form = PhaseForm(instance=phase)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=phase)
        if form.is_valid():
            form.save()
            return redirect('phase_list')
    return render(request, 'object/phase_edit.html', {'form': form})


def search(request):
    q = request.GET.get('q')
    if q:
        posts = ProjectDocument.search().queryset("match", project_description=q)
    else:
        posts = ''
    return render(request, 'object/project_main_list.html', {'posts': posts})


'''
def unit_delete(request, id):
    data = dict()
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        group.is_deleted = True
        group.is_active = False
        group.delete_user_id = request.user.username
        group.deletion_time = datetime.datetime.now().replace(microsecond=0)
        group.save()
        data['form_is_valid'] = True
        groups = Group.objects.filter(is_active=True)
        data['group_list'] = render_to_string('elements/group_list_2.html', {'groups': groups})
    else:
        context = {'group': group}
        data['html_form'] = render_to_string('elements/group_delete.html', context, request=request)

    return JsonResponse(data)
def phase_delete(request, id):
    data = dict()
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        group.is_deleted = True
        group.is_active = False
        group.delete_user_id = request.user.username
        group.deletion_time = datetime.datetime.now().replace(microsecond=0)
        group.save()
        data['form_is_valid'] = True
        groups = Group.objects.filter(is_active=True)
        data['group_list'] = render_to_string('elements/group_list_2.html', {'groups': groups})
    else:
        context = {'group': group}
        data['html_form'] = render_to_string('elements/group_delete.html', context, request=request)

    return JsonResponse(data)
def project_delete(request, id):
    data = dict()
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        group.is_deleted = True
        group.is_active = False
        group.delete_user_id = request.user.username
        group.deletion_time = datetime.datetime.now().replace(microsecond=0)
        group.save()
        data['form_is_valid'] = True
        groups = Group.objects.filter(is_active=True)
        data['group_list'] = render_to_string('elements/group_list_2.html', {'groups': groups})
    else:
        context = {'group': group}
        data['html_form'] = render_to_string('elements/group_delete.html', context, request=request)

    return JsonResponse(data)'''
