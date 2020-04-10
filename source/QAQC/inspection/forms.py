from crispy_forms.layout import Layout
from django import forms
from .models import *
from crispy_forms.helper import FormHelper


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
        self.fields['remarks'].label = 'Remark '
        self.fields['ref_no'].label = 'Ref No'
        self.fields['form_title'].label = 'Form Tittle'

    class Meta:
        model = FormTemplate
        widgets = {
            'form_type_template_id': forms.HiddenInput(),
            'rev': forms.HiddenInput(),
            'form_title': forms.TextInput(
                attrs={'placeholder': 'Eg:FLOOR, WALL, CEILING, DOOR, WINDOW, FIXTURES, M&E'}),
            'remarks': forms.TextInput(
                attrs={'placeholder': 'Form remark(if any)...'}),
        }
        fields = (
            'form_title',
            'ref_no',
            'rev',
            'remarks',
            'form_type_template_id',
        )


class TemplateDetailForm(forms.ModelForm):
    group_id = forms.ModelChoiceField(queryset=Group.objects.filter(is_active=True).order_by('defect_group'),
                                      empty_label='Select Group For Questions')

    def __init__(self, *args, **kwargs):
        super(TemplateDetailForm, self).__init__(*args, **kwargs)
        self.fields['question'].label = ''
        self.fields['is_boolean_question'].label = ''
        self.fields['group_id'].label = 'Defect Group'

    class Meta:
        widgets = {
            'form_template_id': forms.HiddenInput(),
            'legend': forms.HiddenInput(),
            'question_line': forms.HiddenInput(),
            'question': forms.TextInput(
                attrs={'placeholder': 'Enter question here...(Tick if the answering style is True/False.)'}),

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


