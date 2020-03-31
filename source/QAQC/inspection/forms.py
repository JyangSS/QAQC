from django import forms
from .models import *


class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = (
            'element',
            'description',
        )


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'defect_group',
            'description',
            'element_id',
        )


class FormTypeForm(forms.ModelForm):
    class Meta:
        model = FormTypeTemplate
        widgets = {
            'number_series_id': forms.HiddenInput(),
        }
        fields = (
            'form_type',
            'form_description',
        )
        labels = {
            'form_type': 'Form Type Name',
            'form_description': 'Form Short Name',
        }


class NumberSeriesForm(forms.ModelForm):
    class Meta:
        model = NumberSeries
        fields = (
            'series',
            'current',
        )


class FromTemplateForm(forms.ModelForm):
    class Meta:
        model = FormTemplate
        fields = (
            'form_title',
            'ref_no',
            'remarks',
            'form_type_template_id',
        )


class FromDetailsForm(forms.ModelForm):
    class Meta:
        model = TemplateDetail
        fields = (
            'legend',
            'question_line',
            'question',
            'is_boolean_question',
            'group_id',
            'form_template_id',
        )
