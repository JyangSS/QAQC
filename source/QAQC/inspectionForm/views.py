from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect


def element_list(request):
    elements = Element.objects.all()
    groups = Group.objects.all()

    context = {
        'elements': elements,
        'groups': groups,

    }
    return render(request, 'elements/element_list.html', context)


def save_all(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            elements = Element.objects.all()

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
            data['form_is_valid'] = True
            groups = Group.objects.all()
            data['group_list'] = render_to_string('elements/group_list_2.html',
                                                  {'groups': groups})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


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
    return save_all_2(request, form, 'elements/group_create.html')


def element_update(request, id):
    element = get_object_or_404(Element, id=id)
    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)

    else:
        form = ElementForm(instance=element)
    return save_all(request, form, 'elements/element_update.html')


def group_update(request, id):
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)

    else:
        form = GroupForm(instance=group)
    return save_all_2(request, form, 'elements/group_update.html')


def element_delete(request, id):
    data = dict()
    element = get_object_or_404(Element, id=id)
    if request.method == 'POST':
        element.delete()
        data['form_is_valid'] = True
        elements = Element.objects.all()
        data['element_list'] = render_to_string('elements/element_list_2.html', {'elements': elements})
    else:
        context = {'element': element}
        data['html_form'] = render_to_string('elements/element_delete.html', context, request=request)

    return JsonResponse(data)


def group_delete(request, id):
    data = dict()
    group = get_object_or_404(Group, id=id)
    if request.method == 'POST':
        group.delete()
        data['form_is_valid'] = True
        groups = Group.objects.all()
        data['group_list'] = render_to_string('elements/group_list_2.html', {'groups': groups})
    else:
        context = {'group': group}
        data['html_form'] = render_to_string('elements/group_delete.html', context, request=request)

    return JsonResponse(data)


# Create your views here. (KENT)
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


def unitList(request):
    unit = UnitNumber.objects.all()
    return render(request, 'inspectionForm/unitList.html', {'unit': unit})

def projectList(request):
    project = Project.objects.all()
    return render(request,'inspectionForm/projectList.html', {'project': project})

def phaseList(request):
    phase = Phase.objects.all()
    return render(request,'inspectionForm/phaseList.html', {'phase': phase})

def test(request):
    return render(request, 'inspectionForm/test.html')

