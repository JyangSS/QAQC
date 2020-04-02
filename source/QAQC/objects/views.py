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
from django.forms import modelformset_factory


# Create your views here. (KENT)
def company_list(request):
    list = Company.objects.all()

    if request.POST.get('delete'):
        Company.objects.filter(id__in=request.POST.getlist('item')).delete()
        return redirect('company_list')
    context = \
        {'list': list}
    return render(request, 'object/company_list.html', context)


def company_create(request):
    createFormSet = modelformset_factory(Company, fields=('company',), extra=1)
    if request.method == 'POST':
        formset = createFormSet(request.POST, queryset=Company.objects.none(), initial=[{'company': ''}])
        for form in formset:
            if form.is_valid():
                if form.cleaned_data != {}:
                    form.save()
        return redirect('company_list')
    else:
        formset = createFormSet(queryset=Company.objects.none(), initial=[{'company': ''}])

    return render(request, 'object/object_create.html', {'formset': formset})


def company_edit(request, id):
    instance = get_object_or_404(Company, pk=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('company_list')

    else:
        form = CompanyForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form})


def project_list(request, id):
    title = Company.objects.get(pk=id)
    create_id = id
    list = Project.objects.filter(company_id=id)

    if request.POST.get('delete'):
        Project.objects.filter(id__in=request.POST.getlist('item')).delete()
        return redirect(reverse('project_list', kwargs={'id': id}))
    context = \
        {'list': list, 'create_id': create_id, 'title': title}
    return render(request, 'object/project_list.html', context)


def project_create(request, id):
    createFormSet = modelformset_factory(Project, fields=('project_short_form', 'project_description',), extra=1)
    if request.method == 'POST':
        formset = createFormSet(request.POST, queryset=Project.objects.none())
        for form in formset:
            if form.is_valid():
                if form.cleaned_data != {}:
                    instance = form.save(commit=False)
                    instance.company_id = Company.objects.get(pk=id)
                    instance.save()

        return redirect(reverse('project_list', kwargs={'id': id}))
    else:
        formset = createFormSet(queryset=Project.objects.none())

    return render(request, 'object/object_create.html', {'formset': formset})


def project_edit(request, id):
    instance = get_object_or_404(Project, pk=id)
    n = Company.objects.get(project__pk=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('project_list', kwargs={'id': n.pk}))

    else:
        form = ProjectForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form})


def phase_list(request, id):
    title = Project.objects.get(pk=id)
    create_id = id
    list = Phase.objects.filter(project_id=id)

    if request.POST.get('delete'):
        Project.objects.filter(id__in=request.POST.getlist('item')).delete()
        return redirect(reverse('phase_list', kwargs={'id': id}))
    context = \
        {'list': list, 'create_id': create_id, 'title': title}
    return render(request, 'object/phase_list.html', context)


def phase_create(request, id):
    createFormSet = modelformset_factory(Phase, fields=('phase_short_form', 'phase_description',), extra=1)
    if request.method == 'POST':
        formset = createFormSet(request.POST, queryset=Phase.objects.none())
        for form in formset:
            if form.is_valid():
                if form.cleaned_data != {}:
                    instance = form.save(commit=False)
                    instance.project_id = Project.objects.get(pk=id)
                    instance.save()

        return redirect(reverse('phase_list', kwargs={'id': id}))
    else:
        formset = createFormSet(queryset=Phase.objects.none())

    return render(request, 'object/object_create.html', {'formset': formset})


def phase_edit(request, id):
    instance = get_object_or_404(Phase, pk=id)
    n = Project.objects.get(phase__pk=id)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('phase_list', kwargs={'id': n.pk}))

    else:
        form = PhaseForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form})


def unit_list(request, id):
    title = Phase.objects.get(pk=id)
    create_id = id
    list = UnitNumber.objects.filter(phase_id=id)

    if request.POST.get('delete'):
        UnitNumber.objects.filter(id__in=request.POST.getlist('item')).delete()
        return redirect(reverse('unit_list', kwargs={'id': id}))
    context = \
        {'list': list, 'create_id': create_id, 'title': title}
    return render(request, 'object/unit_list.html', context)


def unit_edit(request, id):
    instance = get_object_or_404(UnitNumber, pk=id)
    n = Phase.objects.get(unitnumber__pk=id)
    if request.method == 'POST':
        form = UnitNumberForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('unit_list', kwargs={'id': n.pk}))

    else:
        form = UnitNumberForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form})


# ==================================ignore below====================================================
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

    return render(request, 'object/project_main_list.html',
                  {'add_project': add_project, 'c': c, 'page_title': page_title,
                   'phase': phase, 'add_phase': add_phase})


