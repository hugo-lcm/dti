from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models
import datetime


class Lembrete(models.Model):
    PRIORIDADE_CHOICES = [
        ('A', 'Alta'),
        ('N', 'Normal'),
        ('B', 'Baixa')
    ]

    titulo = models.CharField(max_length=40, null=False, blank=False)
    descricao = models.CharField(max_length=300, null=False, blank=False)
    # com o validators, so vai aceitar datas iguais a do dia atual ou superior
    data = models.DateField(null=False, blank=False, validators=[MinValueValidator(datetime.date.today)])
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
