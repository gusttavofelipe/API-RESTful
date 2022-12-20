from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    comentario = models.TextField(verbose_name='Comentário')
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.usuario.username
