from django.db import models
from alunos.models import Aluno

class Avaliacaofisica(models.Model):
    numero = models.CharField('Número', max_length=100, unique=True)
    peso = models.FloatField('Peso', blank=True, null=True)
    altura = models.FloatField('Altura', blank=True, null=True)
    percentual_gordura = models.FloatField('Percentual gordura', blank=True, null=True)
    massa_magra = models.FloatField('Massa magra', blank=True, null=True)
    imc = models.FloatField('IMC', blank=True, null=True)
    data_avaliacao = models.DateField('Data avaliacao', auto_now_add=True)
    aluno = models.OneToOneField(
        Aluno,
        on_delete=models.CASCADE,
        related_name='avaliacaofisica'
    )

    class Meta:
        verbose_name = 'Avaliacao física'
        verbose_name_plural = 'Avaliações físicas'
        ordering = ['id']

    def str__(self):
        return f'Avaliação de {self.aluno}'

    @property
    def calcular_imc(self):
        if self.peso and self.altura:
            return round(self.peso / (self.altura ** 2), 2)
        return 0