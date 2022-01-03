from rest_framework import viewsets
from artigos_app.models import Autor
from .serializers import AutorSerializer

class AutorViewSet(viewsets.ModelViewSet):
    
    # consulta
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer