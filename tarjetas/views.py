from django.shortcuts import render
from .models import Tarjeta
from cuentas.models import *

def tarjetas(request):
    # Obtener las tarjetas del usuario actual
    tarjetas = Tarjeta.objects.filter(usuario=request.user)
    user = request.user
    cuenta = Cuenta.objects.get(id_cliente = user.id)
    return render(request, 'tarjetas.html', {'tarjetas': tarjetas, 'cuenta':cuenta})