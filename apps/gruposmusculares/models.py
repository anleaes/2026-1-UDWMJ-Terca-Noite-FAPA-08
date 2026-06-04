from django.db import models

# Create your models here.
class Grupomuscular(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Grupo Muscular'
        verbose_name_plural = 'Grupos Musculares'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'