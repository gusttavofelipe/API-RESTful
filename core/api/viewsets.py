from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import PontosTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontosTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        
        # filtrando por query string
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
    

    # @action(methods=['get'], detail=True) 
    # def denounce(self, request, pk=None):
    #     '''
    #     methods - em quais metodos disparar
    #     detail - necessario ou não uma pk na ação da action 
    #     '''
    #     pass

