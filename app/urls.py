from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_lembretes/', listar_lembretes, name='listar_lembretes')
]
