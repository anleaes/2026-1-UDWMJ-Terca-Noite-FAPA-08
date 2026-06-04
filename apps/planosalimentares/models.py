from django.db import models
from alunos.models import Aluno
from nutricionistas.models import Nutricionista

# Create your models here.
class Planoalimentar(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    nome = models.CharField('Nome', max_length=20)
    descricao = models.TextField('Descricao', max_length=200)
    esta_ativo = models.BooleanField('Ativo', default=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Plano Alimentar'
        verbose_name_plural = 'Planos Alimentares'
        ordering =['id']

    def __str__(self):
        return f'{self.nome}' 
