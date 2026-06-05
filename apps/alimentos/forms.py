from django import forms
from .models import Alimento

class AlimentoForm(forms.ModelForm):

    class Meta:
        model = Alimento
        exclude = ()