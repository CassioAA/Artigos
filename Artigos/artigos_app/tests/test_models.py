from django.test import TestCase
from model_mommy import mommy

class ArtigoTestCase(TestCase):

    def setUp(self):
        self.artigo = mommy.make('Artigo')

    def test_str(self):
        self.assertEquals(str(self.artigo), self.artigo.titulo)

class AutorTestCase(TestCase):

    def setUp(self):
        self.autor = mommy.make('Autor')

    def test_str(self):
        self.assertEquals(str(self.autor), 
            self.autor.nome + ' - ' + self.autor.email)