from django.shortcuts import render, redirect
from .form import *


# Create your views here.

def createObject(request):
    if request.method == 'POST':
        unit_number = UnitNumberForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return redirect('createObject')
        elif unit_number.is_valid():
            unit_number.save()
            return redirect('createObject')
    else:
        unit_number = UnitNumberForm()
        project = ProjectForm()
    return render(request, 'inspectionForm/createObject.html', {'unit_number': unit_number, 'project': project})


def createProject(request):
    if request.method == 'POST':
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            return redirect('createObject')
    else:
        project = ProjectForm()
    return render(request, 'inspectionForm/createProject.html', {'project': project})


def createPhase(request):
    if request.method == 'POST':
        phase = PhaseForm(request.POST)
        project = ProjectForm(request.POST)
        if project.is_valid():
            project.save()
            if phase.is_valid():
                phase.save()
            return redirect('createObject')
    else:
        phase = PhaseForm()
        project = ProjectForm()
    return render(request, 'inspectionForm/createPhase.html', {'phase': phase, 'project': project})

def projectList(request):
    unit = UnitNumber.objects.all()
    phase=Phase.objects.all()
    project=Project.objects.all()
    return render(request, 'inspectionForm/projectList.html',{'project': project,'phase':phase,'unit':unit})

def test(request):
    return render(request, 'inspectionForm/test.html')
