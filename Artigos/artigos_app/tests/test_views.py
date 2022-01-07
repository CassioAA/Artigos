from django.test import TestCase
from django.test import Client

from django.urls import reverse_lazy

class IndexTestCase(TestCase):

    def setUp(self):
        self.cliente = Client()

    def test_index(self):
        response = self.client.get(reverse_lazy('index'))
        self.assertEquals(int(response.status_code), 200)