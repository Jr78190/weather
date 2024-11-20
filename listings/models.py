#  le ficher models.py permet de crée la base de donnée, definir les relations et manipuler les données
from django.db import models

class Periode(models.Model):
   debut = models.DateField()  # DateField pour les dates sans information complémentaire 
   fin = models.DateField()

class Meteo(models.Model):
   localisation = models.CharField(max_length=100) # CharField pour des petites chaine de caracteres 
   date = models.DateField() 
   temperature = models.FloatField() # FloatFiel pour des valeurs positives ou négatives 
   humidite = models.FloatField()
   description = models.CharField(max_length=200)

class Activite(models.Model):
    nom = models.CharField(max_length=100)
    distance = models.FloatField()
    localisation = models.CharField(max_length=100)

    
