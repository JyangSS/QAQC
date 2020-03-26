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

    return JsonResponse(data)


# group
def group_list(request, id):
    extra_forms = 1
    element = get_object_or_404(Element, id=id)
    groups = Group.objects.filter(element_id=element.id, is_active=True)
    GroupFormset = inlineformset_factory(Element, Group, fields=('defect_group', 'description',), can_delete=True,
                                         extra=extra_forms)
    formset = GroupFormset(request.POST, instance=element)
    if request.method == 'POST':
        # if 'add' in request.POST and request.POST['add'] == 'true':
        #     formset_dictionary_copy = request.POST.copy()
        #     formset_dictionary_copy['form-TOTAL_FORMS'] =int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
        # formset = GroupFormset(formset_dictionary_copy)
     formset = GroupFormset(request.POST, instance=element)
    if formset.is_valid():
        for group in formset.save(commit=False):
            group.last_modifier_user_id = request.user.username
            group.last_modification_time = datetime.datetime.now().replace(microsecond=0)
            if group.creator_user_id == '':
                group.creator_user_id = request.user.username
                group.creation_time = datetime.datetime.now().replace(microsecond=0)
                formset.save()
                return redirect('group_list', id=id)
    else:
        formset = GroupFormset()
    formset = GroupFormset(instance=element)
    context = {
        'element': element,
        'groups': groups,
        'formset': formset,
    }
    return render(request, 'elements/group_list.html', context)


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
        data['group-list'] = render_to_string('elements/element_list.html', {'groups': groups})
    else:
        context = {'group': group}
        data['html_form'] = render_to_string('elements/element_delete.html', context, request=request)

    return JsonResponse(data)


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
        number.save()
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


def add_forms(request):
    pass
