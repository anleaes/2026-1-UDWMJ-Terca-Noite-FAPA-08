from django.db import models


class CategoriaAlimento(models.Model):

    nome = models.CharField(
        'Nome',
        max_length=100
    )

    descricao = models.TextField(
        'Descrição',
        max_length=300
    )
    
    class Meta:
        verbose_name = 'Categoria de alimento'
        verbose_name_plural = 'Categorias de alimentos'
        ordering = ['id']

    def __str__(self):

        return self.nome
