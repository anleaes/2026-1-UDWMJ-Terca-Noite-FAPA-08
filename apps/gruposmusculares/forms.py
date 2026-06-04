from django import forms
from .models import Grupomuscular

class GrupomuscularForm(forms.ModelForm):

    class Meta:
        model = Grupomuscular
        exclude = ()