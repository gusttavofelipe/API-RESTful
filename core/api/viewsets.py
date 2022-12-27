from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import PontosTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontosTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.all()
    

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste':'list sobrescrito'})

    
    # def create(self, request, *args, **kwargs):
    #     return Response ({'Hello': request.data['visitante']})