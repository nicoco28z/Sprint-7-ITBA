from django import forms

class FormPrestamo(forms.Form):
  monto = forms.DecimalField(
        label='Monto a solicitar',
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
    )
  fecha_inicio = forms.DateTimeField(
        label='Fecha de inicio',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control datetimepicker-input', 'style': 'max-width: 300px;'})
    )
  nombre_cliente = forms.CharField(
        label='Nombre',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 300px; text-center'})
    )
  apellido_cliente = forms.CharField(
        label='Apellido',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
    )
  tipo = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 300px;'})
    )
  