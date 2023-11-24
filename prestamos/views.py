from django.shortcuts import render
from .forms import FormPrestamo
from .models import Prestamo
from movimientos.models import Movimiento
from cuentas.models import Cuenta
from django.core.exceptions import ValidationError


def prestamo(req):
  nombre_cliente = req.session['first_name']
  apellido_cliente = req.session['last_name']
  tipo_cliente = req.session['tipo_cliente']
  id_cliente = req.session['id_cliente']
  if req.method == 'POST':
    form = FormPrestamo(req.POST)
    if form.is_valid():
      info = form.cleaned_data
      monto = info['monto']
      fecha_inicio = info['fecha_inicio']
      nombre_cliente = info['nombre_cliente']
      apellido_cliente = info['apellido_cliente']
      tipo = info['tipo']


      #Obtener la 1er cuenta del cliente
      cuenta = Cuenta.objects.get(id_cliente = id_cliente)

      """Esta parte de validaciones se encuentra hardcodeada, pero podría optimizarse cambiando el modelo de datos"""
      if tipo_cliente == "Classic" and monto > 100000 :
        raise ValidationError("El monto solicitado supera el máximo permitido para este tipo de cliente.")
      
      if tipo_cliente == "Gold" and monto > 300000 :
        raise ValidationError("El monto solicitado supera el máximo permitido para este tipo de cliente.")
      
      if tipo_cliente == "Gold" and monto > 500000 :
        raise ValidationError("El monto solicitado supera el máximo permitido para este tipo de cliente.")

      nuevoPrestamo = Prestamo(
        tipo,
        fecha_inicio,
        monto,
        id_cliente,
        nombre_cliente,
        apellido_cliente
      )
      nuevoPrestamo.save()
      momvimiento = Movimiento(cuenta.id_cuenta, monto, "prestamo | " + tipo)
      momvimiento.save()
    

      cuenta.saldo += monto
      cuenta.save()

  else:
    form = FormPrestamo(initial={'nombre_cliente':nombre_cliente, 'apellido_cliente':apellido_cliente})
  return render(req, 'formPrestamo.html', {'form': form})