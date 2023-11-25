from django.db import models

class Movimiento(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_movimientos = models.CharField(max_length=20, choices=[('ingreso', 'Ingreso'), ('transferencia', 'Transferencia'), ('compra', 'Compra')])