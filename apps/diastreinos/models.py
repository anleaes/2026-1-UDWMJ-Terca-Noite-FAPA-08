from django.db import models
from exercicios.models import Exercicio
from fichastreinos.models import Fichatreino

# Create your models here.
class Diatreino(models.Model):
    dia_treino = models.CharField('Dia de Treino', max_length=1, choices=[
        ('A', 'Treino A'),
        ('B', 'Treino B'),
        ('C', 'Treino C'),
        ('D', 'Treino D'),
        ('E', 'Treino E'),
        ('F', 'Treino F'),
    ])
    serie = models.IntegerField('Serie',null=True, blank=True,default=0)
    repeticao = models.IntegerField('Repeticao',null=True, blank=True,default=0)
    intervalo = models.IntegerField('Intervalo',null=True, blank=True,default=0)
    observacao = models.TextField('Descricao', max_length=200)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE, related_name='exercicios')
    ficha_treino = models.ForeignKey(Fichatreino, on_delete=models.CASCADE, related_name='fichastreinos')

    class Meta:
        verbose_name = 'Dia de treino'
        verbose_name_plural = 'Dias de Treinos'
        ordering =['id']

    def __str__(self):
        return f'{self.id}' 
