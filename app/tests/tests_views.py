from django.test import TestCase
from django.urls import reverse


class UsuarioViewTestCase(TestCase):

    def test_status_code_200_cadastrar_usuario(self):
        response = self.client.get(reverse('cadastrar_usuario'))
        self.assertEqual(response.status_code, 200)

    def test_status_code_200_logar(self):
        response = self.client.get(reverse('logar_usuario'))
        self.assertEqual(response.status_code, 200)

    # def test_status_code_200_deslogar(self):
    #     response = self.client.get(reverse('deslogar_usuario'))
    #     self.assertEqual(response.status_code, 200)

    def test_template_usado_cadastrar_usuario(self):
        response = self.client.get(reverse('cadastrar_usuario'))
        self.assertTemplateUsed(response, 'usuarios/form_usuario.html')

    def test_template_usado_logar(self):
        response = self.client.get(reverse('logar_usuario'))
        self.assertTemplateUsed(response, 'usuarios/login.html')
