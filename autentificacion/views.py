from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def home (request):
    return render(request, 'home.html')

def register (request):
    return render(request, 'register.html')

@login_required
def cliente (request):
    return render(request, 'cliente.html')

def exit(request):
    logout(request)
    return redirect('home')