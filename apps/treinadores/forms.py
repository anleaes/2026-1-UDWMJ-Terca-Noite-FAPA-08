from django import forms
from .models import Treinador

class TreinadorForm(forms.ModelForm):

    class Meta:
        model = Treinador
        exclude = ()