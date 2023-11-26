from django.shortcuts import render, redirect
from .forms import FormPrestamo
from .models import Prestamo
from movimientos.models import Movimiento
from cuentas.models import Cuenta
from django.core.exceptions import ValidationError
from autentificacion.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
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

      """Esta parte de validaciones se encuentra hardcodeada, pero podría optimizarse cambiando el modelo de datos"""
      if tipo_cliente == "Classic" and monto > 100000 :
        print("El monto solicitado supera el máximo permitido para este tipo de cliente.")
        render(req, 'formPrestamo.html', {'form': form})
      
      if tipo_cliente == "Gold" and monto > 300000 :
        print("El monto solicitado supera el máximo permitido para este tipo de cliente.")
        render(req, 'formPrestamo.html', {'form': form})
      
      if tipo_cliente == "Gold" and monto > 500000 :
        print("El monto solicitado supera el máximo permitido para este tipo de cliente.")
        render(req, 'formPrestamo.html', {'form': form})

      cuenta = Cuenta.objects.get(id_cliente = id_cliente)
      cliente = CustomUser.objects.get(id=id_cliente)

      nuevoPrestamo = Prestamo(
        loan_type=tipo,
        fecha_inicio=fecha_inicio,
        loan_total=monto,
        customer_id=cliente,
        customer_name=nombre_cliente,
        customer_lastname=apellido_cliente
      )
      nuevoPrestamo.save()
      momvimiento = Movimiento(nro_cuenta=cuenta, monto=monto, operacion= "prestamo | " + tipo)
      momvimiento.save()
    

      cuenta.saldo += monto
      cuenta.save()

      return redirect(to="home")

  else:
    form = FormPrestamo(initial={'nombre_cliente':nombre_cliente, 'apellido_cliente':apellido_cliente})
  user = req.user
  cuenta = Cuenta.objects.get(id_cliente = user.id)
  return render(req, 'formPrestamo.html', {'form': form, 'cuenta' : cuenta,})