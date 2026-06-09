from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password' , 'email']
        labels = {
            'first_name': 'nome',
            'last_name': 'sobrenome',
            'username': 'nome_usuario',
            'password': 'senha',
        }

class UsuarioAlterarInformacoesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'nome',
            'last_name': 'sobrenome',
        }
