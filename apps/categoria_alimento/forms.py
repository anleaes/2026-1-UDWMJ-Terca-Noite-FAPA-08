from django import forms

from .models import CategoriaAlimento


class CategoriaAlimentoForm(forms.ModelForm):

    class Meta:

        model = CategoriaAlimento

        fields = '__all__'