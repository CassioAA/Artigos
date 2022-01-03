from django.db.models import fields
from artigos_app.models import Autor
from rest_framework import serializers

# serialização do modelo de dado Autor
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('nome', 'endereco', 'site', 'email')