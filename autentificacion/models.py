from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from prestamos.models import Tipo_cliente

class CustomUser(AbstractUser):
    dni = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    ocupacion_laboral = models.CharField(max_length=50, blank=True)
    sueldo_mensual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_user_permissions'
    )

    def __str__(self):
        return self.username
    
class Cliente(models.Model):
    id_cliente = models.ForeignKey(CustomUser, primary_key=True)
    tipo_cuenta = models.ForeignKey(Tipo_cliente, to_field='id_cuenta')