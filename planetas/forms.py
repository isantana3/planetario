from django.forms.fields import CharField
from .models import Planeta
from django.forms import ModelForm, TextInput, ImageField, DecimalField


class PlanetaForm(ModelForm):
    class Meta:
        model = Planeta
        fields = ['name', 'image', 'diameter', 'description']
