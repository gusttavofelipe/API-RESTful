from django.db import models

class Recurso(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Recurso disponibilizado')
    descricao = models.TextField(verbose_name='Descrição')
    horario_func = models.TextField(verbose_name='Horário de funcionamento')
    idade_minima = models.IntegerField()


    def __str__(self):
        return self.nome