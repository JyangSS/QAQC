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

    return render(request, 'object/project_main_list.html',
                  {'c': c, 'page_title_project': page_title_project})


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
        add_phase.fields['project_id'].queryset= Phase.objects.all().order_by('project_id')
    return render(request, 'object/project_main_list.html',
                  {'add_project': add_project, 'c': c, 'page_title': page_title,
                   'phase': phase,'add_phase':add_phase})


def unit_main_list(request, id):
    unit = UnitNumber.objects.filter(phase_id=id)
    c = Company.objects.all()
    page_title = Phase.objects.get(pk=id)

    if request.method == 'POST':
        add_project = ProjectForm(request.POST)
        add_unit=UnitNumberForm(request.POST or None, initial={'phase_id':id})

        if add_project.is_valid():
            n = add_project.save()
            n.pk
            return redirect(reverse('project_main_list', kwargs={'id': n.pk}))
        elif add_unit.is_valid():
            add_unit.save()
            return redirect(reverse('unit_main_list', kwargs={'id': id}))
    else:
        add_project = ProjectForm()
        add_unit=UnitNumberForm(initial={'phase_id':id})
    return render(request, 'object/unit_main_list.html',
                  {'unit': unit, 'add_project': add_project, 'c': c,'page_title':page_title,'add_unit':add_unit})


def project_delete(request, id):
    data = dict()
    project = get_object_or_404(Project, id=id)
    if request.method == 'POST':
        project.is_deleted = True
        project.is_active = False
        project.delete_user_id = request.user.username
        project.deletion_time = datetime.datetime.now().replace(microsecond=0)
        project.save()
        data['form_is_valid'] = True
        projects = Project.objects.filter(is_active=True)
        # data['project_main_list'] = render_to_string('object/unit_list.html', {'projects': projects})
    else:
        context = {'project': project}
        data['html_form'] = render_to_string('object/project_delete.html', context, request=request)

    return JsonResponse(data)


def phase_delete(request, id):
    data = dict()
    phase = get_object_or_404(Phase, id=id)
    if request.method == 'POST':
        phase.is_deleted = True
        phase.is_active = False
        phase.delete_user_id = request.user.username
        phase.deletion_time = datetime.datetime.now().replace(microsecond=0)
        phase.save()
        data['form_is_valid'] = True
        phases = Project.objects.filter(is_active=True)
        data['project_main_list'] = render_to_string('object/phase_list.html', {'phase': phases})
    else:
        context = {'phase': phase}
        data['html_form'] = render_to_string('object/phase_delete.html', context, request=request)
    return JsonResponse(data)
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
    '''
