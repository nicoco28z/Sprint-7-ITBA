from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('cliente/', cliente, name='cliente'),
    path('logout/', exit, name='exit')
]
