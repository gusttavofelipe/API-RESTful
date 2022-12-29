from rest_framework.viewsets import ModelViewSet
from atracoes.models import Recurso
from .serializers import RecursoSerializer



class RecursoViewSet(ModelViewSet):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

    # django_filters
    filterset_fields = ('id', 'nome', 'descricao', )