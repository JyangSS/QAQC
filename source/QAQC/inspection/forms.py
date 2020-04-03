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
        widgets = {
            'element_id': forms.HiddenInput(),
        }
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
            'number_series_id',
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


