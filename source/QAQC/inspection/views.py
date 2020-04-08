from django.db import transaction
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import render
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
    groups = Group.objects.filter(is_active=True, element_id=element.id)
    context = {
        'element': element,
        'groups': groups,
    }
    return render(request, 'groups/group_list.html', context)


def save_group(request, form, template_name, id):
    element = Element.objects.get(pk=id)
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
            groups = Group.objects.filter(is_active=True, element_id=obj.element_id)
            data['element_list'] = render_to_string('groups/group_list_2.html',
                                                    {'groups': groups})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
        'element': element,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def save_group2(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = Group.objects.order_by('-pk')[0]
            data['form_is_valid'] = True
            groups = Group.objects.filter(is_active=True, element_id=obj.element_id)
            data['element_list'] = render_to_string('groups/group_list_2.html',
                                                    {'groups': groups})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def group_create(request, id):
    element = Element.objects.get(pk=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, initial={'element_id': id})
    else:
        form = GroupForm(initial={'element_id': id})

    return save_group(request, form, 'groups/group_create.html', int(element.id))


def group_update(request, id):
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        group.last_modifier_user_id = request.user.username
        group.last_modification_time = datetime.datetime.now().replace(microsecond=0)

    else:
        form = GroupForm(instance=group)
    return save_group2(request, form, 'groups/group_update.html')


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
        groups = Group.objects.filter(is_active=True, element_id=group.element_id)
        data['element_list'] = render_to_string('groups/group_list_2.html', {'groups': groups})
    else:
        context = {'group': group}
        data['html_form'] = render_to_string('groups/group_delete.html', context, request=request)
    return JsonResponse(data)


# forms type
def form_type(request, id):
    number = NumberSeries.objects.get(pk=id)
    types = FormTypeTemplate.objects.filter(is_active=True, number_series_id=number)
    context = {
        'types': types,
        'number': number,
    }
    return render(request, 'forms_type/form_type.html', context)


def save_type(request, form, template_name, id):
    number = NumberSeries.objects.get(pk=id)
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
            data['form_is_valid'] = True
            types = FormTypeTemplate.objects.filter(is_active=True, number_series_id=obj.number_series_id)
            data['element_list'] = render_to_string('forms_type/form_type_2.html',
                                                    {'types': types})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
        'number': number,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def save_type2(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = FormTypeTemplate.objects.order_by('-pk')[0]
            data['form_is_valid'] = True
            types = FormTypeTemplate.objects.filter(is_active=True, number_series_id=obj.number_series_id)
            data['element_list'] = render_to_string('forms_type/form_type_2.html',
                                                    {'types': types})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def form_type_create(request, id):
    number = NumberSeries.objects.get(pk=id)
    if request.method == 'POST':
        form = FormTypeForm(request.POST, initial={'number_series_id': id})
    else:
        form = FormTypeForm(initial={'number_series_id': id})

    return save_type(request, form, 'forms_type/form_type_create.html', int(number.id))


def form_type_update(request, id):
    type = get_object_or_404(FormTypeTemplate, id=id)
    if request.method == 'POST':
        form = FormTypeForm(request.POST, instance=type)
        type.last_modifier_user_id = request.user.username
        type.last_modification_time = datetime.datetime.now().replace(microsecond=0)

    else:
        form = FormTypeForm(instance=type)
    return save_type2(request, form, 'forms_type/form_type_update.html')


def form_type_delete(request, id):
    data = dict()
    type = get_object_or_404(FormTypeTemplate, id=id)
    if request.method == 'POST':
        type.is_deleted = True
        type.is_active = False
        type.delete_user_id = request.user.username
        type.deletion_time = datetime.datetime.now().replace(microsecond=0)
        type.save()
        data['form_is_valid'] = True
        types = FormTypeTemplate.objects.filter(is_active=True, number_series_id=type.number_series_id)
        data['element_list'] = render_to_string('forms_type/form_type_2.html', {'types': types})
    else:
        context = {'type': type}
        data['html_form'] = render_to_string('forms_type/form_type_delete.html', context, request=request)
    return JsonResponse(data)


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


# forms
def templates(request, id):
    type = FormTypeTemplate.objects.get(pk=id)
    number = NumberSeries.objects.get(series=type.number_series_id)
    templates = FormTemplate.objects.filter(is_active=True, form_type_template_id=type)
    context = {
        'type': type,
        'number': number,
        'templates': templates,

    }
    return render(request, 'forms/form_list.html', context)


def template_create(request, id):
    type = FormTypeTemplate.objects.get(pk=id)
    count = FormTemplate.objects.filter(form_type_template_id=type.id).count()
    ref = type.form_description + "/" + str('{0:03}'.format(count + 1))
    if request.method == 'POST':
        form = TemplateForm(request.POST, initial={'form_type_template_id': id, 'ref_no': ref,'rev':1 ,})

    else:
        form = TemplateForm(initial={'form_type_template_id': id, 'ref_no': ref,'rev':1, })

    return save_template(request, form, 'forms/form_create.html', int(type.id))


def save_template(request, form, template_name, id):
    type = FormTypeTemplate.objects.get(pk=id)
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            obj = FormTemplate.objects.order_by('-pk')[0]
            if obj.creator_user_id == '':
                obj.creator_user_id = request.user.username
                obj.creation_time = datetime.datetime.now().replace(microsecond=0)
                obj.last_modifier_user_id = request.user.username
                obj.last_modification_time = datetime.datetime.now().replace(microsecond=0)
                obj.save()
            data['form_is_valid'] = True
            templates = FormTemplate.objects.filter(is_active=True, form_type_template_id=obj.form_type_template_id)
            data['element_list'] = render_to_string('forms/form_list_2.html',
                                                    {'templates': templates})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
        'type': type,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def template_delete(request, id):
    data = dict()
    template = get_object_or_404(FormTemplate, id=id)
    if request.method == 'POST':
        template.is_deleted = True
        template.is_active = False
        template.delete_user_id = request.user.username
        template.deletion_time = datetime.datetime.now().replace(microsecond=0)
        template.save()
        data['form_is_valid'] = True
        templates = FormTemplate.objects.filter(is_active=True, form_type_template_id=template.form_type_template_id)
        data['element_list'] = render_to_string('forms/form_list_2.html', {'templates': templates})
    else:
        context = {'template': template}
        data['html_form'] = render_to_string('forms/form_delete.html', context, request=request)

    return JsonResponse(data)


def save_template2(request, form,id,template_name):
    data = dict()
    template = get_object_or_404(FormTemplate, id=id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            templates = FormTemplate.objects.filter(is_active=True, form_type_template_id=template.form_type_template_id)
            data['element_list'] = render_to_string('forms/form_list_2.html',
                                                    {'templates': templates})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)



def template_update(request, id):
    template = get_object_or_404(FormTemplate, id=id)
    if request.method == 'POST':
        form = TemplateForm(request.POST, instance=template)
        template.last_modifier_user_id = request.user.username
        template.last_modification_time = datetime.datetime.now().replace(microsecond=0)

    else:
        form = TemplateForm(instance=template)
    return save_template2(request, form,template.id, 'forms/form_update.html')
