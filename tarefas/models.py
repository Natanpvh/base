from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(u'Nome:', max_length=100)
    descricao = models.TextField(u'Descrição:')
