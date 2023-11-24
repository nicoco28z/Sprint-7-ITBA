from typing import Any
from django.db import models
from cuentas.models import Cuenta

class Movimiento(models.Model):
  id_mov = models.AutoField(primary_key=True)
  nro_cuenta = models.ForeignKey(Cuenta, to_field='id_cuenta')
  monto = models.DecimalField(decimal_places=2)
  operacion = models.CharField(max_length=100)
  fecha_hora = models.DateTimeField(auto_now_add=True)

  def __init__(self, nro_cuenta, monto, operacion ):
    self.nro_cuenta = nro_cuenta
    self.monto = monto
    self.operacion = operacion