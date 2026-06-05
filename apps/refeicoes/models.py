from django.db import models
from alimentos.models import Alimento
from planosalimentares.models import Planoalimentar

# Create your models here.
class Refeicao(models.Model):
    dia_refeicao = models.CharField('Dia de Refeicao', max_length=1, choices=[
        ('1', 'Desjejum'),
        ('2', 'Lanche da Manha'),
        ('3', 'Almoco'),
        ('4', 'Lanche da Tarde'),
        ('5', 'Jantar'),
        ('6', 'Ceia'),
    ])
    observacao = models.TextField('Descricao', max_length=200)
    quantidade_gramas = models.FloatField('Quantidade em gramas', null=True, blank=True, default=0)
    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, related_name='alimentos')
    plano_alimentar = models.ForeignKey(Planoalimentar, on_delete=models.CASCADE, related_name='planosalimentares')

    class Meta:
        verbose_name = 'Dia de Refeicao'
        verbose_name_plural = 'Dias de Refeicoes'
        ordering =['id']

    def __str__(self):
        return f'{self.id}'

    @property
    def total_proteinas(self):
        if self.alimento.porcao_referencia_gramas > 0:
            multiplicador = self.quantidade_gramas / self.alimento.porcao_referencia_gramas
            return round(self.alimento.proteina * multiplicador, 2)
        return 0

    @property
    def total_carboidratos(self):
        if self.alimento.porcao_referencia_gramas > 0:
            multiplicador = self.quantidade_gramas / self.alimento.porcao_referencia_gramas
            return round(self.alimento.carboidrato * multiplicador, 2)
        return 0

    @property
    def total_gorduras(self):
        if self.alimento.porcao_referencia_gramas > 0:
            multiplicador = self.quantidade_gramas / self.alimento.porcao_referencia_gramas
            return round(self.alimento.gordura * multiplicador, 2)
        return 0

    @property
    def total_calorias(self):
        if self.alimento.porcao_referencia_gramas > 0:
            multiplicador = self.quantidade_gramas / self.alimento.porcao_referencia_gramas
            return round(self.alimento.calorias * multiplicador, 2)
        return 0
