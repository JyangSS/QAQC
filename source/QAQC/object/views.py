from typing import Dict

from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
import datetime
from django.http import JsonResponse
from django.views.generic import View



# Create your views here. (KENT)


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
    return render(request, 'inspection/unitList.html',
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
    return render(request, 'inspection/projectList.html', {'project': project, 'add_project': add_project})


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
    return render(request, 'inspection/phaseList.html',
                  {'phase': phase, 'add_phase': add_phase, 'project': project})


def edit_unit(request, id):
    unit = UnitNumber.objects.get(pk=id)
    form = UnitNumberForm(instance=unit)
    if request.method == 'POST':
        form = UnitNumberForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    return render(request, 'inspection/editUnit.html', {'form': form})


def edit_project(request, id):
    project = Project.objects.get(pk=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    return render(request, 'inspection/editProject.html', {'form': form})


def edit_phase(request, id):
    phase = Phase.objects.get(pk=id)
    form = PhaseForm(instance=phase)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=phase)
        if form.is_valid():
            form.save()
            return redirect('phase_list')
    return render(request, 'inspection/editPhase.html', {'form': form})
