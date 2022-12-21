from django.db import models
from atracoes.models import Recurso
from comentarios.models import Comentario
from avaliacoes.models import Avalicao
from enderecos.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    aprovado = models.BooleanField(default=False)
    recurso = models.ManyToManyField(Recurso)
    comentario = models.ManyToManyField(Comentario)
    avalicao = models.ManyToManyField(Avalicao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
