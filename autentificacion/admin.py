from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','dni','email','telefono','fecha_nacimiento','ocupacion_laboral','sueldo_mensual')

@admin.register(Tipo_cliente)
class TipoClienteAdmin(admin.ModelAdmin):
    list_display=("tarjeta_debito","retiros_realizados","chequera","tipo")