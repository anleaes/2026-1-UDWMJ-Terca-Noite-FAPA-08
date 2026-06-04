from django.db import models

# Create your models here.
class Categoriaalimento(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Categoria Alimento'
        verbose_name_plural = 'Categorias Alimentos'
        ordering =['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'