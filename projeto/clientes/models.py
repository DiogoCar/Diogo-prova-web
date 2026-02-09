from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    dataDeCriacao = models.DateTimeField(auto_now_add=True)
    numeroDeTelefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
