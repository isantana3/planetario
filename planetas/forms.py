
from django import forms
from .models import Planeta


class PlanetaForm(forms.ModelForm):
    class Meta:
        model = Planeta
        fields = ['name', 'diameter', 'description',]