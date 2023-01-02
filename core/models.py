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
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
        )
    image = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True, verbose_name='Imagem')


    @property
    def descricao_completa2(self):
        # função com nome escolhido para 
        # o campo decorado com @property,
        # adicionar em fields do serializer
        return '%s - %s' % (self.nome, self.descricao)


    def __str__(self):
        return self.nome
