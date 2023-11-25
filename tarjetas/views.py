from django.shortcuts import render
from .models import Tarjeta

def tarjetas(request):
    # Obtener las tarjetas del usuario actual
    tarjetas = Tarjeta.objects.filter(usuario=request.user)
    return render(request, 'tarjetas.html', {'tarjetas': tarjetas})