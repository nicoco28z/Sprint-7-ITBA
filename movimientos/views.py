from django.shortcuts import render
from .models import Movimiento
from cuentas.models import *

def movimientos_usuario(request):
    movimientos = Movimiento.objects.all()
    user = request.user
    cuenta = Cuenta.objects.get(id_cliente = user.id)
    return render(request, 'movimientos.html', {'movimientos': movimientos, 'cuenta':cuenta})

