from django.db import models
from gruposmusculares.models import Grupomuscular

# Create your models here.
class Exercicio(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=200)
    esta_ativo = models.BooleanField('Ativo', default=False)
    foto = models.ImageField('Foto', upload_to='fotos')
    grupomuscular = models.ForeignKey(Grupomuscular, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering =['id']

    def __str__(self):
        return f'{self.nome}'