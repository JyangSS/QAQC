from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


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


COMPANY_CHOICES = [
    ('Huayang', 'Huayang'),
    ('Agro-Mod Industries', 'Agro-Mod Industries'),
    ('Bison Holdings', 'Bison Holdings'),
    ('G Land Development', 'G Land Development'),
]


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
