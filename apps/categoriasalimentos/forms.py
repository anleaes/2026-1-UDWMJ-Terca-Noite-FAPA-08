from django import forms
from .models import Categoriaalimento

class CategoriaalimentoForm(forms.ModelForm):

    class Meta:
        model = Categoriaalimento
        exclude = ()