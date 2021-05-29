from django.test import TestCase


def add_num(num):
    return num + 1


class SimplesTestCase(TestCase):

    def __init__(self):
        self.message = 'Inicio do TestCase'

    def setUp(self):
        print(self.message)

    def test_add_num(self):
        valor = add_num(43)
        self.assertTrue(valor == 44)
