from source.QAQC.objects.forms import *
from django.shortcuts import render, redirect


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
    return render(request, 'inspection/unit_list.html',
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
    return render(request, 'inspection/project_list.html', {'project': project, 'add_project': add_project})


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
    return render(request, 'inspection/phase_list.html',
                  {'phase': phase, 'add_phase': add_phase, 'project': project})


def edit_unit(request, id):
    unit = UnitNumber.objects.get(pk=id)
    form = UnitNumberForm(instance=unit)
    if request.method == 'POST':
        form = UnitNumberForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    return render(request, 'inspection/unit_edit.html', {'form': form})


def edit_project(request, id):
    project = Project.objects.get(pk=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    return render(request, 'inspection/project_edit.html', {'form': form})


def edit_phase(request, id):
    phase = Phase.objects.get(pk=id)
    form = PhaseForm(instance=phase)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=phase)
        if form.is_valid():
            form.save()
            return redirect('phase_list')
    return render(request, 'inspection/phase_edit.html', {'form': form})
