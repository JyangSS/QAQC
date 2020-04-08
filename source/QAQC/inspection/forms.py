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


class TemplateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TemplateForm, self).__init__(*args, **kwargs)
        self.fields['ref_no'].widget.attrs['readonly'] = True

    class Meta:
        model = FormTemplate
        widgets = {
            'form_type_template_id': forms.HiddenInput(),
            'rev': forms.HiddenInput(),
        }
        fields = (
            'form_title',
            'ref_no',
            'rev',
            'remarks',
            'form_type_template_id',
        )


class TemplateDetailForm(forms.ModelForm):
    class Meta:
        widgets = {
            'form_template_id': forms.HiddenInput(),
            'legend': forms.HiddenInput(),
            'question_line': forms.HiddenInput(),
        }
        model = TemplateDetail
        fields = (
            'group_id',
            'form_template_id',
            'legend',
            'question_line',
            'question',
            'is_boolean_question',
        )

