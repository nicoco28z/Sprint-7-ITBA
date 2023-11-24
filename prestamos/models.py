from django.db import models
from autentificacion.models import CustomUser

# Create your models here.
class Prestamo(models.Model):
  loan_id = models.AutoField(primary_key=True)
  loan_type = models.CharField()
  loan_date = models.DateTimeField(auto_now_add=True)
  loan_total = models.DecimalField(decimal_places=2)
  customer_id = models.ForeignKey(CustomUser, to_field='id') #Revisar


class Tipo_cliente(models.Model):
  id_cuenta = models.AutoField(primary_key=True)
  tarjeta_debito = models.PositiveSmallIntegerField()
  retiros_realizados = models.PositiveSmallIntegerField()
  chequera = models.PositiveSmallIntegerField()
  tipo = models.CharField()