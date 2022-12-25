from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avalicao
from .serializers import AvalicaoSerializer


class AvalicaoViewSet(ModelViewSet):
    queryset = Avalicao.objects.all()
    serializer_class = AvalicaoSerializer