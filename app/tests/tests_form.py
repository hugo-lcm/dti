from django.test import TestCase
from ..forms import LembreteForm


class LembreteFormTestCase(TestCase):

    def test_lembrete_form_valido(self):
        form = LembreteForm(data={
            'titulo': 'lembrete999',
            'descricao': 'lembrete para testes',
            'data': '2022-08-21',
            'prioridade': 'A'
        })
        self.assertTrue(form.is_valid())

    def test_lembrete_form_invalido(self):
        form = LembreteForm(data={})
        self.assertFalse(form.is_valid())
