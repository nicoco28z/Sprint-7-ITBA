from django.db import models
from django.contrib.auth.models import User

class Tarjeta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=16)
    titular = models.CharField(max_length=255)
    fecha_expiracion = models.DateField()

    def __str__(self):
        return f'{self.numero} - {self.titular}'