from django.shortcuts import render
from .models import Movimiento
# Create your views here.

def movimientos_usuario(request):
    movimientos = Movimiento.objects.all()
    return render(request, 'movimientos.html', {'movimientos': movimientos})

