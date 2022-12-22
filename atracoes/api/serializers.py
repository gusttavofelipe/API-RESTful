from rest_framework.serializers import ModelSerializer
from atracoes.models import Recurso

class RecursoSerializer(ModelSerializer):
    class Meta:
        model = Recurso
        fields = '__all__'