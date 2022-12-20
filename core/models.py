from django.db import models
from atracoes.models import Recursos

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    aprovado = models.BooleanField(default=False)
    recurso = models.ManyToManyField(Recursos)


    def __str__(self):
        return self.nome
