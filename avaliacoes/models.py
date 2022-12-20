from django.db import models
from django.contrib.auth.models import User

class Avalicao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    comentario = models.TextField(null=True, blank=True, verbose_name='Comentário')
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.usuario.username