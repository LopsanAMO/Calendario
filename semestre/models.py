from django.db import models

class Semestre(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    inicio = models.DateField(blank=False, null=False)
    fin = models.DateField(blank=False, null=False)

class Vacaciones(models.Model):
	nombre = models.CharField(blank=False, null=False, max_length=100)
	semestre = models.ForeignKey(Semestre, blank=False, null=False)
	inicio = models.DateField(blank=False, null=False)
	fin = models.DateField(blank=False, null=False)
