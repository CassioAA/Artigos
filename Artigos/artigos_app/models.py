from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome + ' - ' + self.email

class Artigo(models.Model):

    # A chave estrangeira do relacionamento
    # de artigos com autor. Quando um dado
    # de Atuor for deletado, os artigos referentes
    # a ele também serão deletados
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    publicado_em = models.DateField(auto_now=True)
    atualizado_em = models.DateField(auto_now_add=True)
    texto = TextField()

    def __str__(self):
        return self.titulo