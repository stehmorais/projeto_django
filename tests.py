from django.test import TestCase


class Feriado(TestCase):
    def test_natal(self):
        response = self.client.get('/')
        self.assertContains(response, 'É Natal')

    def test_tiradentes(self):
        response = self.client.get('/')
        self.assertContains(response, 'É Tiradentes')

    def test_nao_feriado(self):
        response = self.client.get('/')
        self.assertContains(response, 'Não é nenhum dos feriados')
