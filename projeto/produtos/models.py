from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=False)
    precoDeCompra = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    precoDeVenda = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    dataDeValidade = models.DateField(null=False, blank=False)


    def __str__(self):
        return self.nome

