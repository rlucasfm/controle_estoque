from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    quantidade = models.PositiveIntegerField('Quantidade',default=0)
    valor = models.DecimalField('Valor',default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome