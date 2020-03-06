from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project_description',
            'project_short_form',
        ]
class PhaseForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'phase_description',
            'phase_short_form',
        ]
class UnitNumberForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'block',
            'level',
            'unit_number',
        ]


