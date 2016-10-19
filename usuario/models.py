from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.ForeignKey(User, null=False, blank=False)
    boleta = models.CharField(null=False ,blank=False, max_length=10)

class qr(models.Model):
    user models.ForeignKey(User, null=False, blank=False)
    codigo = models.ImageField(null=True, blak=True)
