from rest_framework import viewsets
from artigos_app.models import Autor,Artigo
from .serializers import AutorSerializer,ArtigoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AutorViewSet(viewsets.ModelViewSet):
    # se o usuario não estiver logado, não 
    # poderá fazer alterações(PUT) nos dados da 
    # API nem inserir (POST) dados, apenas ler (GET)
    # outras permissões: AllowAny, IsAuthenticated
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class ArtigoViewSet(viewsets.ModelViewSet):
    # consulta
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
