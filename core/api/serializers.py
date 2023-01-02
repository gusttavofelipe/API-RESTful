from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import RecursoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvalicaoSerializer
from rest_framework.serializers import SerializerMethodField


class PontosTuristicoSerializer(ModelSerializer):
    # relacoes aninhadas:
    # many=True apenas em relacionamentos ManyToMany
    endereco = EnderecoSerializer()
    recurso = RecursoSerializer(many=True) 
    comentario = ComentarioSerializer(many=True)
    avalicao = AvalicaoSerializer(many=True)

    # campo adicional , disponivel apenas para leitura
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'recurso',
            'comentario', 'avalicao', 'endereco', 'image',
            'descricao_completa', 'descricao_completa2'
        )

    
        # get + nome do campo adicional
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
            