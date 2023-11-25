from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    dni = models.CharField(max_length=20, blank=False)
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
    
class Tipo_cliente(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tarjeta_debito = models.PositiveSmallIntegerField()
    retiros_realizados = models.PositiveSmallIntegerField()
    chequera = models.PositiveSmallIntegerField()
    tipo = models.CharField(max_length=100, unique=True)

class Cliente(models.Model):
    id_cliente = models.ForeignKey(CustomUser, to_field="id", primary_key=True, on_delete=models.DO_NOTHING)
    tipo_cliente = models.ForeignKey(Tipo_cliente, to_field='id_tipo', on_delete=models.DO_NOTHING)

