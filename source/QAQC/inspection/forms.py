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

