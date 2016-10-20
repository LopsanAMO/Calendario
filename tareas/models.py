from django.db import models
from materias.models import Materia
from django.contrib.auth.models import User

class Tarea(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    materia = models.ForeignKey(Materia, blank=False, null=False)
    fecha_entrega = models.DateField(blank=False, null=False)
    prioridad = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.CharField(max_length=250, blank=False, null=False)

class Alarma(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tarea = models.ForeignKey(Tarea, blank=False, null=False)

class Hora(models.Model):
    hora = models.DateField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    alarma = models.ForeignKey(Alarma, blank=False, null=False,)


class Compa(models.Model):
    nombre = models.ForeignKey(User, blank=True, null=True)
    tarea = models.ForeignKey(Tarea, blank=True, null=True)
