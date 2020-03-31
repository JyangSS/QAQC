from django.db import transaction
from django.forms import modelformset_factory, inlineformset_factory
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
import datetime
from django.http import JsonResponse


# show all objects in table
def element_list(request):
    elements = Element.objects.filter(is_active=True)
    context = {
        'elements': elements,
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
                obj.last_modifier_user_id = request.user.username
                obj.last_modification_time = datetime.datetime.now().replace(microsecond=0)
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


# create
def element_create(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
    else:
        form = ElementForm()
    return save_all(request, form, 'elements/element_create.html')


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


# group
def group_list(request, id):
    element = Element.objects.get(pk=id)
    groups = Group.objects.filter(is_active=True, element_id=element)

    context = {
        'element': element,
        'groups': groups, }

    return render(request, 'elements/group_list.html', context)


def save_group(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = Group.objects.order_by('-pk')[0]
            if obj.creator_user_id == '':
                obj.creator_user_id = request.user.username
                obj.creation_time = datetime.datetime.now().replace(microsecond=0)
                obj.last_modifier_user_id = request.user.username
                obj.last_modification_time = datetime.datetime.now().replace(microsecond=0)
                obj.save()
            data['form_is_valid'] = True
            groups = Group.objects.filter(is_active=True)
            data['element_list'] = render_to_string('elements/group_list_2.html',
                                                    {'groups': groups})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
    else:
        form = GroupForm()
    return save_group(request,form, 'elements/group_create.html')


# def group_delete(request, id):
#     data = dict()
#     group = get_object_or_404(Group, id=id)
#     if request.method == 'POST':
#         group.is_deleted = True
#         group.is_active = False
#         group.delete_user_id = request.user.username
#         group.deletion_time = datetime.datetime.now().replace(microsecond=0)
#         group.save()
#         data['form_is_valid'] = True
#         groups = Group.objects.filter(is_active=True)
#         data['group-list'] = render_to_string('elements/element_list.html', {'groups': groups})
#     else:
#         context = {'group': group}
#         data['html_form'] = render_to_string('elements/element_delete.html', context, request=request)
#
#     return JsonResponse(data)


# form type
def form_type(request):
    types = FormTypeTemplate.objects.filter(is_active=True)
    context = {
        'types': types,
    }
    return render(request, 'forms/form_type.html', context)


def save_form_type(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = FormTypeTemplate.objects.order_by('-pk')[0]
            if obj.creator_user_id == '':
                obj.creator_user_id = request.user.username
                obj.creation_time = datetime.datetime.now().replace(microsecond=0)
                obj.last_modifier_user_id = request.user.username
                obj.last_modification_time = datetime.datetime.now().replace(microsecond=0)
                obj.save()
                number = NumberSeries(series=obj.form_description,
                                      current=1,
                                      form_type_template_id=obj,
                                      creator_user_id=request.user.username,
                                      creation_time=datetime.datetime.now().replace(microsecond=0),
                                      last_modifier_user_id=request.user.username,
                                      last_modification_time=datetime.datetime.now().replace(microsecond=0)
                                      )
                number.save(force_insert=True)
            data['form_is_valid'] = True
            types = FormTypeTemplate.objects.filter(is_active=True)
            data['form_list'] = render_to_string('forms/form_type_2.html',
                                                 {'types': types, 'obj': obj})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def form_type_create(request):
    if request.method == 'POST':
        form = FormTypeForm(request.POST)
    else:
        form = FormTypeForm()
    return save_form_type(request, form, 'forms/form_type_create.html')


def form_type_update(request, id):
    type = get_object_or_404(FormTypeTemplate, id=id)
    if request.method == 'POST':
        form = FormTypeForm(request.POST, instance=type)
        type.last_modifier_user_id = request.user.username
        type.last_modification_time = datetime.datetime.now().replace(microsecond=0)
        number = NumberSeries.objects.get(form_type_template_id=type.pk)
        number.series = request.POST.get('form_description')
        number.last_modifier_user_id = request.user.username
        number.last_modification_time = datetime.datetime.now().replace(microsecond=0)
        number.sav
    else:
        form = FormTypeForm(instance=type)
    return save_form_type(request, form, 'forms/form_type_update.html')


def form_type_delete(request, id):
    data = dict()
    type = get_object_or_404(FormTypeTemplate, id=id)
    if request.method == 'POST':
        type.is_deleted = True
        type.is_active = False
        type.delete_user_id = request.user.username
        type.deletion_time = datetime.datetime.now().replace(microsecond=0)
        type.save()
        number = NumberSeries.objects.get(form_type_template_id=type.pk)
        number.is_deleted = True
        number.is_active = False
        number.delete_user_id = request.user.username
        number.deletion_time = datetime.datetime.now().replace(microsecond=0)
        number.save()
        data['form_is_valid'] = True
        types = FormTypeTemplate.objects.filter(is_active=True)
        data['form_list'] = render_to_string('forms/form_type_2.html', {'types': types})
    else:
        context = {'type': type}
        data['html_form'] = render_to_string('forms/form_type_delete.html', context, request=request)

    return JsonResponse(data)


# form and form details
def forms(request, id):
    type = get_object_or_404(FormTypeTemplate, id=id)
    all_form = FormTemplate.objects.filter(form_type_template_id=type)
    context = {
        'type': type,
        'all_form': all_form,
    }
    return render(request, 'forms/forms.html', context)


# number series
def number_series_list(request):
    numbers = NumberSeries.objects.filter(is_active=True)
    context = {
        'numbers': numbers,
    }
    return render(request, 'number_series/number_series_list.html', context)


def save_number(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = NumberSeries.objects.order_by('-pk')[0]
            if obj.creator_user_id == '':
                obj.creator_user_id = request.user.username
                obj.creation_time = datetime.datetime.now().replace(microsecond=0)
                obj.last_modifier_user_id = request.user.username
                obj.last_modification_time = datetime.datetime.now().replace(microsecond=0)
                obj.save()
            data['form_is_valid'] = True
            numbers = NumberSeries.objects.filter(is_active=True)
            data['element_list'] = render_to_string('number_series/number_series_list_2.html',
                                                    {'numbers': numbers})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


# create
def number_series_create(request):
    if request.method == 'POST':
        form = NumberSeriesForm(request.POST)
    else:
        form = NumberSeriesForm()
    return save_number(request, form, 'number_series/number_series_create.html')


# update
def number_series_update(request, id):
    number_series = get_object_or_404(NumberSeries, id=id)
    if request.method == 'POST':
        form = NumberSeriesForm(request.POST, instance=number_series)
        number_series.last_modifier_user_id = request.user.username
        number_series.last_modification_time = datetime.datetime.now().replace(microsecond=0)

    else:
        form = NumberSeriesForm(instance=number_series)
    return save_number(request, form, 'number_series/number_series_update.html')


# delete
def number_series_delete(request, id):
    data = dict()
    number_series = get_object_or_404(NumberSeries, id=id)
    if request.method == 'POST':
        number_series.is_deleted = True
        number_series.is_active = False
        number_series.delete_user_id = request.user.username
        number_series.deletion_time = datetime.datetime.now().replace(microsecond=0)
        number_series.save()
        data['form_is_valid'] = True
        numbers = NumberSeries.objects.filter(is_active=True)
        data['element_list'] = render_to_string('number_series/number_series_list_2.html', {'numbers': numbers})
    else:
        context = {'number_series': number_series}
        data['html_form'] = render_to_string('number_series/number_series_delete.html', context, request=request)

    return JsonResponse(data)
