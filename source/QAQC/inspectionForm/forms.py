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
