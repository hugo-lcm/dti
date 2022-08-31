# faz as validações antes de inserir no bd e cria o formulário de cadastro de uma classe

from django import forms
from .models import Lembrete


class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = '__all__'  # todos os campos do models serão validados
