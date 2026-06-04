from django.db import models

# Create your models here.
class Fichamedica(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=200) 
    
    class Meta:
        verbose_name = 'Ficha Medica'
        verbose_name_plural = 'Fichas Medicas'
        ordering =['id']

    def __str__(self):
        return f'{self.nome}'