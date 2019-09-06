from django.db import models


class Musica(models.Model):
    nome_da_musica = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    link_musica = models.CharField(max_length=255)

