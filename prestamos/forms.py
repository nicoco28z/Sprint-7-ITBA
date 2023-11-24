from django import forms

class FormPrestamo(forms.Form):
  monto = forms.DecimalField(label='Monto a solicitar', decimal_places=2)
  fecha_inicio = forms.DateTimeField(label='Fecha de inicio')
  nombre_cliente = forms.CharField(label='Nombre', max_length=50)
  apellido_cliente = forms.CharField(label='Apellido', max_length=50)
  tipo = forms.CharField(max_length=50) #Ver si no cambiamos por un campo seleccionable

  