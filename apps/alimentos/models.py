from django.db import models
from categoriasalimentos.models import Categoriaalimento

# Create your models here.
class Alimento(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=200)
    porcao_referencia_gramas = models.FloatField('Porção de Referência (g)', default=100.0)
    calorias = models.FloatField('Calorias', default=0)
    proteina = models.FloatField('Proteina', default=0)
    carboidrato = models.FloatField('Carboidrato', default=0)
    gordura = models.FloatField('Gordura', default=0)
    esta_ativo = models.BooleanField('Ativo', default=False)
    foto = models.ImageField('Foto', upload_to='fotos')
    categoriaalimento = models.ForeignKey(Categoriaalimento, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'