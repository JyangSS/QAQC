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
from django.contrib import messages

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


def register_new_block(request):
    if request.method == 'POST':
        form = RegisterNewBlockForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            id = obj.phase_id.id
            i = request.POST.get('max_level')
            j = request.POST.get('max_unit_per_level')
            s1 = request.POST.get('specific_level_1')
            ss1 = request.POST.get('specific_unit_1')
            s2 = request.POST.get('specific_level_2')
            ss2 = request.POST.get('specific_unit_2')
            s3 = request.POST.get('specific_level_3')
            ss3 = request.POST.get('specific_unit_3')

            if not i or not j or not s1 or not ss1 or not s2 or not ss2 or not s3 or not ss3 or (int(ss1)>int(i)) or (int(ss2)>int(i)) or (int(ss3)>int(i)):
                messages.error(request, 'Error!!! You might not completely fill up the form or the specific level is greater than max level!!!')
                return redirect('register_new_block')
            else:
                for a in range(1,int(i)+1):
                    if (int(s1) == a):
                        for b in range(1,int(ss1)+1):
                            form = RegisterNewBlockForm(request.POST)
                            obj = form.save(commit=False)
                            obj.level = int(a)
                            obj.unit_number = int(b)
                            obj.save()

                    elif (int(s2) == a):
                        for b in range(1,int(ss2)+1):
                            form = RegisterNewBlockForm(request.POST)
                            obj = form.save(commit=False)
                            obj.level = int(a)
                            obj.unit_number = int(b)
                            obj.save()
                    elif (int(s3) == a):
                        for b in range(1, int(ss3) + 1):
                            form = RegisterNewBlockForm(request.POST)
                            obj = form.save(commit=False)
                            obj.level = int(a)
                            obj.unit_number = int(b)
                            obj.save()

                    else:
                        for b in range(1,int(j)+1):
                            form = RegisterNewBlockForm(request.POST)
                            obj = form.save(commit=False)
                            obj.level = int(a)
                            obj.unit_number=int(b)
                            obj.save()
                else:
                    return redirect(reverse('register_unit_list_phase',kwargs={'id':id}))

    else:
            form = RegisterNewBlockForm()
            return render(request,'object/register_new_block.html',{'form':form})


def register_unit_list_all(request):
    list = UnitNumber.objects.all()
    select=Project.objects.all()

    return render(request,'object/register_unit_list.html', {'list':list,'select':select})


'''def register_unit_list_project(request,id):
    list = UnitNumber.objects.filter(phase_id__project_id=id)
    select=Project.objects.all()

    return render(request,'object/register_unit_list.html', {'list':list,'select':select})'''

def register_unit_list_phase(request,id):
    list = UnitNumber.objects.filter(phase_id=id)
    select=Project.objects.all()

    return render(request,'object/register_unit_list.html', {'list':list,'select':select})






