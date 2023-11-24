from django.db import models
from autentificacion.models import Cliente

class Cuenta(models.Model):
  id_cuenta = models.AutoField(primary_key=True, null=False)
  nro_cuenta = models.PositiveIntegerField(null=False)
  id_cliente = models.ForeignKey(Cliente, to_field='id_cliente', on_delete=models.DO_NOTHING)
  saldo = models.DecimalField(decimal_places=2, max_digits=10)
  iban = models.TextField(max_length=150)