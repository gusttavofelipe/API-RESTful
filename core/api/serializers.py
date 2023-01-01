from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import RecursoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvalicaoSerializer

class PontosTuristicoSerializer(ModelSerializer):
    # relacioes aninhadas ()
    # many=True apenas em relacionamentos ManyToMany
    endereco = EnderecoSerializer()
    recurso = RecursoSerializer(many=True) 
    comentario = ComentarioSerializer(many=True)
    avalicao = AvalicaoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = "__all__"