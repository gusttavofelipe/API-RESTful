from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import PontosTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontosTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.all()
    

    def list(self, request, *args, **kwargs): # dispara no endpoint 
        return super().list(request, *args, **kwargs)

    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


    def  retrieve(self, request, *args, **kwargs): # dispara num recurso do endpoint 
        return super().retrieve(request, *args, **kwargs)


    def update(self, request, *args, **kwargs): # atualiza um recurso/objeto inteiro
        return super().update(request, *args, **kwargs)


    def partial_update(self, request, *args, **kwargs): # atualiza parcialmente/partes de um recurso/objeto 
        return super().partial_update(request, *args, **kwargs)

    
    # @action(methods=['get'], detail=True) 
    # def denounce(self, request, pk=None):
    #     '''methods - em quais metodos disparar
    #        detail - necessario ou não uma pk na ação da action '''
    #     pass

