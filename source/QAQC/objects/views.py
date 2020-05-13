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
from string import ascii_uppercase
from inspection.models import *


# Create your views here. (KENT)
def company_list(request):
    list = Company.objects.all()
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
    delete_company = Company.objects.filter(pk=id)
    if request.method == 'POST':

        form = CompanyForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('company_list')

    else:
        form = CompanyForm(instance=instance)

        return render(request, 'object/object_edit.html', {'form': form,'delete_company':delete_company})

def company_delete(request,id):
    delete=Company.objects.get(pk=id)
    delete.delete()
    return redirect('company_list')


def project_list(request, id):
    title = Company.objects.get(pk=id)
    create_id = id
    list = Project.objects.filter(company_id=id)
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
    delete_project=Project.objects.filter(pk=id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('project_list', kwargs={'id': n.pk}))

    else:
        form = ProjectForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form,'delete_project':delete_project})

def project_delete(request,id):
    delete=Project.objects.get(pk=id)
    n=Company.objects.get(project__pk=id)
    delete.delete()
    return redirect(reverse('project_list', kwargs={'id': n.pk}))


def phase_list(request, id):
    title = Project.objects.get(pk=id)
    list = Phase.objects.filter(project_id=id)
    create_id=title.pk
    context = \
        {'list': list, 'create_id': create_id, 'title': title}
    return render(request, 'object/phase_list.html', context)


def phase_create(request, id):
    createFormSet = modelformset_factory(Phase, fields=('phase_short_form', 'phase_description','inspection_object',), extra=1)
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
                            return redirect('company_list')
    else:
        formset = createFormSet(queryset=Phase.objects.none())

    return render(request, 'object/object_create.html', {'formset': formset})


def phase_edit(request, id):
    instance = get_object_or_404(Phase, pk=id)
    n = Project.objects.get(phase__pk=id)
    delete_phase=Phase.objects.filter(pk=id)
    if request.method == 'POST':
        form = PhaseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('phase_list', kwargs={'id': n.pk}))

    else:
        form = PhaseForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form,'delete_phase':delete_phase})

def phase_delete(request,id):
    delete=Phase.objects.get(pk=id)
    n = Project.objects.get(phase__pk=id)
    delete.delete()
    return redirect(reverse('phase_list', kwargs={'id': n.pk}))


def unit_list(request, id):
    title = Phase.objects.get(pk=id)
    create_id = id
    list = UnitNumber.objects.filter(phase_id=id)

    context = \
        {'list': list, 'create_id': create_id, 'title': title}
    return render(request, 'object/unit_list.html', context)


def unit_edit(request, id):
    instance = get_object_or_404(UnitNumber, pk=id)
    n = Phase.objects.get(unitnumber__pk=id)
    delete_unit=UnitNumber.objects.filter(pk=id)
    if request.method == 'POST':
        form = UnitNumberForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(reverse('unit_list', kwargs={'id': n.pk}))

    else:
        form = UnitNumberForm(instance=instance)
        return render(request, 'object/object_edit.html', {'form': form,'delete_unit':delete_unit})

def unit_delete(request,id):
    delete=UnitNumber.objects.get(pk=id)
    n = Phase.objects.get(unitnumber__pk=id)
    delete.delete()
    return redirect(reverse('unit_list', kwargs={'id': n.pk}))

def register_new_block(request):
    if request.method == 'POST':
        form = RegisterNewBlockForm(request.POST)
        if form.is_valid():
            i = request.POST.get('max_level')
            j = request.POST.get('max_unit_per_level')
            r=FormTemplate.objects.all().count()
            x = UnitNumber.objects.last()
            x=x.pk
            if not i or not j :
                messages.error(request, 'Error!!! You might not completely fill up the form !!!')
                return redirect('register_new_block')
            else:
                for a in range(1,int(i)+1):
                        for b in range(1,int(j)+1):
                            form = RegisterNewBlockForm(request.POST)
                            obj = form.save(commit=False)
                            obj.level = str('{0:02}'.format(int(a)))
                            obj.unit_number=str('{0:02}'.format(int(b)))
                            obj.inspection_object=obj.phase_id.inspection_object+"-"+obj.block+"-"+str('{0:02}'.format(int(a)))+"-"+str('{0:02}'.format(int(b)))
                            for g in range(1,x+1):
                                 if UnitNumber.objects.filter(pk=int(g)).exists():
                                     validation =UnitNumber.objects.get(pk=int(g))
                                     if obj.inspection_object == validation.inspection_object:
                                             messages.error(request, 'Error!!! The inspect code is duplicated !!! Please check there are no duplicated record have fill in.')
                                             return redirect('register_new_block')
                                 else:
                                     continue
                            else:
                                obj.save()
                                for x in range(1,int(r)+1):
                                      Inspection01.objects.create(unit_number_id=UnitNumber.objects.latest('id'),inspection_count=0, form_template_id=FormTemplate.objects.get(pk=x))
                else:
                    return redirect('register_unit_list_all')

    else:
            form = RegisterNewBlockForm()
            return render(request,'register_unit/register_new_block.html',{'form':form})


def register_unit_list_all(request):
    list = UnitNumber.objects.all()
    select=Project.objects.all()
    if request.POST.get('delete'):
        UnitNumber.objects.filter(id__in=request.POST.getlist('item')).delete()
        return redirect('register_unit_list_all')
    return render(request,'register_unit/register_unit_list.html', {'list':list,'select':select})




