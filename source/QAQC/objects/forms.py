from django import forms
from .models import *
from crispy_forms.helper import FormHelper

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company',

        ]
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'company_id',
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
