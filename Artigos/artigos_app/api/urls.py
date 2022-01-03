from django.urls import path, include
from .views import AutorViewSet
from rest_framework import routers

# instanciando a rota
router = routers.DefaultRouter()

# registro da rota e a sua respectiva view
router.register('autor', AutorViewSet)

urlpatterns = [
    path('', include(router.urls))
]