from django.shortcuts import render, redirect
from cuentas.models import Cuenta
from autentificacion.models import Cliente, Tipo_cliente


# Create your views here.
def perfil(req):
    user = req.user
    cliente = Cliente.objects.get(id_cliente_id = user.id)
    tipo_cliente = Tipo_cliente.objects.get(id_tipo = cliente.tipo_cliente.id_tipo)
    cuenta = Cuenta.objects.get(id_cliente = user.id)

    if req.method == 'POST':
        nuevo_mail = req.POST.get('nuevoMail')
        if nuevo_mail: user.email = nuevo_mail

        nueva_profesion = req.POST.get('nuevaProfesion')
        if nueva_profesion: user.ocupacion_laboral = nueva_profesion

        nuevo_sueldo = req.POST.get('nuevoSueldo')
        if nuevo_sueldo: user.sueldo_mensual = nuevo_sueldo

        user.save()

        if 'solicitar_mejora' in req.POST:
            if tipo_cliente.tipo == "Classic":
                cliente.tipo_cliente = Tipo_cliente.objects.get(tipo = "Gold")
            elif tipo_cliente.tipo == "Gold":
                cliente.tipo_cliente = Tipo_cliente.objects.get(tipo = "Black")
            cliente.save()
        
        return redirect('perfil')
    
    return render(req, 'perfil.html', {'user': user, 'tipo_cliente': tipo_cliente, 'cuenta': cuenta})