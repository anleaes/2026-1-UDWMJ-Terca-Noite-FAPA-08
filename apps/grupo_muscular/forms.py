from django import forms
from .models import CategoriaGrupoMuscular

class GrupoMuscularForm(forms.ModelForm):

    class Meta:
        model = CategoriaGrupoMuscular
        exclude = ()