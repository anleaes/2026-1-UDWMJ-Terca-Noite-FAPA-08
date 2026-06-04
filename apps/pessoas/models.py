from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=100) 
    data_nascimento = models.DateField('Data de Nascimento')
    email = models.EmailField('E-mail',null=False, blank=False)
    endereco = models.CharField('Endereco', max_length=200)   
    telefone = models.CharField('Telefone celular', max_length=20)    
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'