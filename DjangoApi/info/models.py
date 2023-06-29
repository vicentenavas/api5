from django.db import models
from django.contrib.postgres.fields import ArrayField


class Servizio(models.Model):
    servizioId = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


   

class Descrizione(models.Model):
    # Cambia el nombre del campo a 'id' en lugar de 'descrizioneId'
    id = models.AutoField(primary_key=True)
    servizio = models.ForeignKey(Servizio, on_delete=models.CASCADE, related_name='descrizioni')
    descrizione = models.CharField(max_length=100)

class Img(models.Model):
    # Cambia el nombre del campo a 'id' en lugar de 'descrizioneId'
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)

class SiOcuppa(models.Model):
    # Cambia el nombre del campo a 'id' en lugar de 'descrizioneId'
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=100)



class Socio(models.Model): 
    socioId = models.AutoField(primary_key=True)
    nome = models.CharField( max_length=25)
    info = models.CharField( max_length=70)