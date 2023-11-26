from typing import Any
from django.db import models
from cuentas.models import Cuenta

class Movimiento(models.Model):
  id_mov = models.AutoField(primary_key=True)
  nro_cuenta = models.ForeignKey(Cuenta, to_field='id_cuenta', on_delete=models.DO_NOTHING)
  monto = models.DecimalField(decimal_places=2, max_digits=10)
  operacion = models.CharField(max_length=100)
  fecha_hora = models.DateTimeField(auto_now_add=True)
