from django.db import models
from pessoas.models import Pessoa

# Create your models here.
class Treinador(Pessoa):
    registroCREF = models.TextField('Registro CREF', max_length=100) 
    tipo_treinamento = models.TextField('Tipo de Treinamento', max_length=100) 

    class Meta:
        verbose_name = 'Treinador'
        verbose_name_plural = 'Treinadores'
        ordering =['id']

    def __str__(self):
        return super().nome
        # ou pode ser usado "return super().__str__()"
