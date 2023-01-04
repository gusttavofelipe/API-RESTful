from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import RecursoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvalicaoSerializer
from rest_framework.serializers import SerializerMethodField
from atracoes.models import Recurso
from enderecos.models import Endereco


class PontosTuristicoSerializer(ModelSerializer):
    # relacoes aninhadas:
    # many=True apenas em relacionamentos ManyToMany
    endereco = EnderecoSerializer()
    recurso = RecursoSerializer(many=True,) 
    comentario = ComentarioSerializer(many=True, read_only=True)
    avalicao = AvalicaoSerializer(many=True, read_only=True)

    # campo adicional , disponivel apenas para leitura
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'recurso',
            'comentario', 'avalicao', 'endereco', 'image',
            'descricao_completa', 'descricao_completa2'
        )


    def cria_recursos(self, recursos, ponto) :
        for recurso in recursos:
            rec = Recurso.objects.create(**recurso)
            ponto.recurso.add(rec)

    def create(self, validated_data):
        recurso = validated_data['recurso']
        del validated_data['recurso']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_recursos(recurso, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save() # salvar apos modificação
        return ponto


        # get + nome do campo adicional
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
            