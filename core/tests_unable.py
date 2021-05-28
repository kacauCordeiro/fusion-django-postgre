from django.test import TestCase


def add_num(num):
    return num + 1


class SimplesTestCase(TestCase):

    def setUp(self):
        print('Inicio do TestCase')

    def test_add_num(self):
        valor = add_num(43)
        self.assertTrue(valor == 44)
