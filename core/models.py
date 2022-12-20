from django.db import models

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    provado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
