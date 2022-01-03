from artigos_app.models import Autor,Artigo
from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        # id para a identificação do dado
        fields = ('id','nome','endereco','site','email')

class ArtigoSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    class Meta:
        model = Artigo
        fields = ('titulo','publicado_em','atualizado_em','texto','autor')
