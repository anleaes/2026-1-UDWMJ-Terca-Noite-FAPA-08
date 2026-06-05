from django.db import models
from alunos.models import Aluno
from treinadores.models import Treinador

# Create your models here.
class Fichatreino(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    nome = models.CharField('Nome', max_length=20)
    descricao = models.TextField('Descricao', max_length=200)
    esta_ativo = models.BooleanField('Ativo', default=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Ficha de Treino'
        verbose_name_plural = 'Fichas de Treinos'
        ordering =['id']

    def __str__(self):
        return f'{self.nome}' 
