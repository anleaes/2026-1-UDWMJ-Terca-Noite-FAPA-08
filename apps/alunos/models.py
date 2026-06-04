from django.db import models
from pessoas.models import Pessoa
from fichasmedicas.models import Fichamedica

# Create your models here.
class Aluno(Pessoa):
    genero = models.CharField('Genero', max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    meta = models.TextField('Meta', max_length=100)
    fichamedica = models.ManyToManyField(Fichamedica, verbose_name="Fichas Medicas")
    
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering =['id']

    def __str__(self):
        return super().nome
        # ou pode ser usado "return super().__str__()"