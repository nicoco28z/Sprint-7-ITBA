from django.db import models
from autentificacion.models import CustomUser

# Create your models here.
class Prestamo(models.Model):
  loan_id = models.AutoField(primary_key=True)
  loan_type = models.CharField(max_length=100)
  loan_date = models.DateTimeField(auto_now_add=True)
  fecha_inicio = models.DateTimeField()
  loan_total = models.DecimalField(decimal_places=2, max_digits=10)
  customer_id = models.ForeignKey(CustomUser, to_field='id', on_delete = models.DO_NOTHING) #Revisar
  customer_name = models.CharField(max_length=50)
  customer_lastname = models.CharField(max_length=50)


