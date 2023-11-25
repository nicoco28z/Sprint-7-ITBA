from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from autentificacion.forms import CustomUserCreationForm, CustomAuthenticationForm
from cuentas.models import Cuenta
from .models import *

class RegisterView(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            
            tipoCliente = Tipo_cliente.objects.get(tipo = "Classic")
            cliente = Cliente(id_cliente= user, tipo_cliente=tipoCliente)
            cliente.save()

            cuenta = Cuenta.objects.create(id_cliente = cliente, nro_cuenta = 1, saldo = 0, iban= "Tu Mama")
            cuenta.save()

            return redirect('home')

        return render(request, 'register.html', {'form': form})

class LoginView(View):

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("Usuario autenticado con éxito")
            return redirect('home')
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class HomeView(View):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'home.html')