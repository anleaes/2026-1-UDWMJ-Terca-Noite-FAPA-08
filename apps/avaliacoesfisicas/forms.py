from django import forms
from .models import Avaliacaofisica
from alunos.models import Aluno

class AvaliacaofisicaForm(forms.ModelForm):

    class Meta:
        model = Avaliacaofisica
        exclude = ('numero', 'imc', 'data_avaliacao')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['aluno'].queryset = Aluno.objects.filter(avaliacaofisica__isnull=True)
