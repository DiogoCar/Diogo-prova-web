from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    valorLimite = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    cidade = models.CharField(max_length=100, blank=False)
    estado = models.CharField(max_length=100, blank=False)
    numeroDeTelefone = models.CharField(max_length=20, blank=False)
    categoria = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome

