from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_lembretes/', listar_lembretes, name='listar_lembretes'),
    path('cadastrar_lembrete/', cadastrar_lembrete, name='cadastrar_lembrete'),
    path('editar_lembrete/<int:id>', editar_lembrete, name='editar_lembrete'),
    path('excluir_lembrete/<int:id>', excluir_lembrete, name='excluir_lembrete')
]
