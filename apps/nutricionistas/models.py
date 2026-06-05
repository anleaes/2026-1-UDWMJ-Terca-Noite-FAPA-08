from django.db import models
from pessoas.models import Pessoa

# Create your models here.
class Nutricionista(Pessoa):
    registroCRN = models.TextField('Registro CRN', max_length=100) 
    abordagem_nutricional = models.TextField('Abordagem Nutricional', max_length=100) 

    class Meta:
        verbose_name = 'Nutricionista'
        verbose_name_plural = 'Nutricionistas'
        ordering =['id']

    def __str__(self):
        return super().nome
        # ou pode ser usado "return super().__str__()"
