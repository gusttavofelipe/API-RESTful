from rest_framework.serializers import ModelSerializer
from atracoes.models import Recurso

class RecursoSerializer(ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'image', )