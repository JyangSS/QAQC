from typing import Dict
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
import datetime
from django.http import JsonResponse
from django.views.generic import View


# Create your views here. (KENT)
def project_main_list_empty(request):
    c = Company.objects.all()
    page_title_project = None

    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        if add_project.is_valid():
            n = add_project.save()
            n.pk
            return redirect(reverse('project_main_list', kwargs={'id': n.pk}))
    else:
        add_project = ProjectForm()
    return render(request, 'object/project_main_list.html',
                  {'c': c, 'page_title_project': page_title_project, 'add_project': add_project})


def project_main_list(request, id):
    c = Company.objects.all()
    phase = Phase.objects.filter(project_id=id)
    page_title = Project.objects.get(pk=id)

    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        add_phase = PhaseForm(request.POST or None)

        if add_project.is_valid():
            n = add_project.save()
            n.pk
            return redirect(reverse('project_main_list', kwargs={'id': n.pk}))
        elif add_phase.is_valid():
            add_phase.save()
            return redirect(reverse('project_main_list', kwargs={'id': id}))
    else:
        add_project = ProjectForm()
        add_phase = PhaseForm(initial={'project_id': id})
        # add_phase.fields['project_id'].queryset= Phase.objects.all().order_by('project_id')
    return render(request, 'object/project_main_list.html',
                  {'add_project': add_project, 'c': c, 'page_title': page_title,
                   'phase': phase, 'add_phase': add_phase})


def unit_main_list(request, id):
    unit = UnitNumber.objects.filter(phase_id=id)
    c = Company.objects.all()
    page_title = Phase.objects.get(pk=id)

    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        add_unit = UnitNumberForm(request.POST or None, initial={'phase_id': id})

        if add_project.is_valid():
            n = add_project.save()
            n.pk
            return redirect(reverse('project_main_list', kwargs={'id': n.pk}))
        elif add_unit.is_valid():
            add_unit.save()
            return redirect(reverse('unit_main_list', kwargs={'id': id}))
    else:
        add_project = ProjectForm()
        add_unit = UnitNumberForm(initial={'phase_id': id})
    return render(request, 'object/unit_main_list.html',
                  {'unit': unit, 'add_project': add_project, 'c': c, 'page_title': page_title, 'add_unit': add_unit})


def phase_edit(request, id=None):
    instance = get_object_or_404(Phase, pk=id)
    n = Project.objects.get(phase__pk=id)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('project_main_list', kwargs={'id': n.pk}))
        #   form.last_modifier_user_id = request.user.username
        #  form.last_modification_time = datetime.datetime.now().replace(microsecond=0)
    else:
        form = PhaseForm(instance=instance)
        return render(request, 'object/phase_edit.html', {'form': form})


def phase_delete(request, id):
    n = Project.objects.get(phase__pk=id)
    phase = get_object_or_404(Phase, id=id)
    phase.delete()
    return redirect(reverse('project_main_list', kwargs={'id': n.pk}))
