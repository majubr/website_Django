from django.db import models


# Create your models here.
class Especies(models.Model):
    objects = None
    Classe = models.CharField(max_length=30)
    Ordem = models.CharField(max_length=30)
    Familia = models.CharField(max_length=30)
    Genero = models.CharField(max_length=30)
    Especie = models.CharField(max_length=30)
    Nome_popular = models.CharField(max_length=30)
    Data_da_coleta = models.CharField(max_length=30)
    Hora_da_coleta = models.CharField(max_length=30)
    Datum = models.CharField(max_length=30)
    Coordenada_x = models.CharField(max_length=30)
    Coordenada_y = models.CharField(max_length=30)
    Metodo_de_coleta = models.CharField(max_length=30)
    Tipo_de_registro = models.CharField(max_length=30)
    Responsavel_pela_coleta = models.CharField(max_length=30)
