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
    element_id = forms.ModelChoiceField(queryset=Element.objects.filter(is_active=True))

    class Meta:
        model = Group
        fields = (
            'defect_group',
            'description',
            'element_id',
        )


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project_description',
            'project_short_form',
        ]


class UnitNumberForm(forms.ModelForm):
    class Meta:
        model = UnitNumber
        fields = [
            'phase_id',
            'block',
            'level',
            'unit_number',
        ]

    helper = FormHelper()
    helper.form_method = 'POST'


class PhaseForm(forms.ModelForm):
    class Meta:
        model = Phase
        fields = [
            'project_id',
            'phase_description',
            'phase_short_form',
        ]

    helper = FormHelper()
    helper.form_method = 'POST'
