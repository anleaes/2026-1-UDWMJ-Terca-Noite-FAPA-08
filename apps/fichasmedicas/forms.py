from django import forms
from .models import Fichamedica

class FichamedicaForm(forms.ModelForm):

    class Meta:
        model = Fichamedica
        exclude = ()