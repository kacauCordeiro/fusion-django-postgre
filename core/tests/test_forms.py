from django.test import TestCase

from core.forms import ContatoForms


class ContatoFormsTestCase(TestCase):

    def setUp(self):
        self.nome = 'nome'
        self.email = 'email@teste.com'
        self.assunto = 'assunto'
        self.mensagem = 'mensagem'
        self.dados = {
            'nome': self.nome, 'email': self.email, 'assunto': self.assunto, 'mensagem': self.mensagem
        }
        self.form = ContatoForms(data=self.dados)

    def test_send_email(self):
        form1 = ContatoForms(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)







