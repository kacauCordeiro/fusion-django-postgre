from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'kauane',
            'email': 'meuemail@gmail.com',
            'assunto': 'meu assunto',
            'mensagem': 'qualquer mensagem'
        }

        self.incorrect_dados = {
            'nome': 'kauane',
            'assunto': 'meu assunto',
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data=self.incorrect_dados)
        self.assertEquals(request.status_code, 200)
