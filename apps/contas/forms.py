from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        # 1. Use os nomes de campo originais do Django em inglês
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        
        # 2. Use 'labels' para traduzir o que vai aparecer no formulário HTML
        labels = {
            'first_name': 'nome',
            'last_name': 'sobrenome',
            'username': 'usuario',
            'password': 'senha',
            'email': 'email'
        }

class UsuarioMudarInformacoesForm(forms.ModelForm):
    class Meta:
        model = User
        # 1. Use os nomes de campo originais do Django em inglês
        fields = ['first_name', 'last_name','email']
        
        # 2. Use 'labels' para traduzir o que vai aparecer no formulário HTML
        labels = {
            'first_name': 'nome',
            'last_name': 'sobrenome',
            'email': 'email'
        }
