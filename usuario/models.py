from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, null=False, blank=False)
    tipo = models.CharField(null=False, blank=False, max_length=100)

class qr(models.Model):
    user = models.OneToOneField(User, null=False, blank=False)
    codigo = models.ImageField(null=True, blank=True)
