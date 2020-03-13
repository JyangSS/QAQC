from typing import Dict

from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
import datetime
from django.http import JsonResponse
from django.views.generic import View



# show all objects in table
def element_list(request):
    elements = Element.objects.filter(is_active=True)
    groups = Group.objects.filter(is_active=True)
    context = {
        'elements': elements,
        'groups': groups,

    }
    return render(request, 'elements/element_list.html', context)


# save created object and updated object
def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = Element.objects.order_by('-pk')[0]
            if obj.creator_user_id == '':
                obj.creator_user_id = request.user.username
                obj.creation_time = datetime.datetime.now().replace(microsecond=0)
                obj.save()
            data['form_is_valid'] = True
            elements = Element.objects.filter(is_active=True)
            data['element_list'] = render_to_string('elements/element_list_2.html',
                                                    {'elements': elements})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def save_all_2(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = Group.objects.order_by('-pk')[0]
            if obj.creator_user_id == '':
                obj.creator_user_id = request.user.username
                obj.creation_time = datetime.datetime.now().replace(microsecond=0)
                obj.save()
            data['form_is_valid'] = True
            groups = Group.objects.filter(is_active=True)
            data['group_list'] = render_to_string('elements/group_list_2.html',
                                                  {'groups': groups})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# create
def element_create(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
    else:
        form = ElementForm()
    return save_all(request, form, 'elements/element_create.html')


def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.user)

    else:
        form = GroupForm()
    return save_all_2(request, form, 'elements/group_create.html')


# update
def element_update(request, id):

    element = get_object_or_404(Element, id=id)
    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)
        element.last_modifier_user_id = request.user.username
        element.last_modification_time = datetime.datetime.now().replace(microsecond=0)

    else:
        form = ElementForm(instance=element)
    return save_all(request, form, 'elements/element_update.html')


def group_update(request, id):

    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        group.last_modifier_user_id = request.user.username
        group.last_modification_time = datetime.datetime.now().replace(microsecond=0)

    else:
        form = GroupForm(instance=group)
    return save_all_2(request, form, 'elements/group_update.html')


# delete
def element_delete(request, id):
    data = dict()
    element = get_object_or_404(Element, id=id)
    if request.method == 'POST':
        element.is_deleted = True
        element.is_active = False
        element.delete_user_id = request.user.username
        element.deletion_time = datetime.datetime.now().replace(microsecond=0)
        element.save()
        data['form_is_valid'] = True
        elements = Element.objects.filter(is_active=True)
        data['element_list'] = render_to_string('elements/element_list_2.html', {'elements': elements})
    else:
        context = {'element': element}
        data['html_form'] = render_to_string('elements/element_delete.html', context, request=request)

    return JsonResponse(data)


def group_delete(request, id):
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
    return render(request, 'inspectionForm/unitList.html',
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
    return render(request, 'inspectionForm/projectList.html', {'project': project, 'add_project': add_project})


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
    return render(request, 'inspectionForm/phaseList.html',
                  {'phase': phase, 'add_phase': add_phase, 'project': project})


def edit_unit(request, id):
    unit = UnitNumber.objects.get(pk=id)
    form = UnitNumberForm(instance=unit)
    if request.method == 'POST':
        form = UnitNumberForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('unit_list')
    return render(request, 'inspectionForm/editUnit.html', {'form': form})


def edit_project(request, id):
    project = Project.objects.get(pk=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    return render(request, 'inspectionForm/editProject.html', {'form': form})


def edit_phase(request, id):
    phase = Phase.objects.get(pk=id)
    form = PhaseForm(instance=phase)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=phase)
        if form.is_valid():
            form.save()
            return redirect('phase_list')
    return render(request, 'inspectionForm/editPhase.html', {'form': form})


