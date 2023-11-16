from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','nombre','apellido','dni','email','telefono','fecha_nacimiento','ocupacion_laboral','sueldo_mensual')