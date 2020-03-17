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
    }
    return render(request, 'elements/element_list.html', context)


def group_list(request, id):
    element = get_object_or_404(Element, id=id)
    groups = Group.objects.filter(element_id=id)
    context = {
        'element': element,
        'groups': groups,
    }
    return render(request, 'elements/group_list.html', context)


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


def save_all2(request, form, template_name):
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
        form = GroupForm(request.POST)
    else:
        form = GroupForm()
    return save_all(request, form, 'elements/group_create.html')


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
    return save_all(request, form, 'elements/group_create.html')


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

