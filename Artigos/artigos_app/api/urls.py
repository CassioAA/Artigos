from django.urls import path,include
from .views import AutorViewSet,ArtigoViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# rota para a visualização dos autores
router.register('autor',AutorViewSet)
# rota para a visualização dos artigos
router.register('artigo',ArtigoViewSet)


urlpatterns = [
    path('',include(router.urls))
]