# faz as validações antes de inserir no bd e cria o formulário de cadastro de uma classe

from django import forms
from .models import Lembrete


class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        exclude = ('usuario', )
        # todos os campos do models serão validados, exceto o que foi passado no exclude
        fields = '__all__'
