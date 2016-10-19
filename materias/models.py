from django.db import models
from django.contrib.auth.models import User

class Horario(models.Moldel):
    user = models.OneToOneField(User, null=False, blank=False)
    id_horario = models.CharField(blank=True, max_length=16)


class Materia(models.Model):
    nombre = models.CharField(blank=True, max_length=100)
    profesor = models.OneToOneField(User, blank=True, null=True, related_name='profes')
    horario = models.ForeignKey(Horario, blank=False, null=False, related_name='materias')

class Horas(models.Model):
    hora = models.DateTimeField(blank=False, null=False)
    fecha = models.DateTimeField(blank=False, null=False)
    materia = models.ForeignKey(Materia, blank=False, null=False, related_name='horas')
