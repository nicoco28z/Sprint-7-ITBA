from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    dni = forms.IntegerField(min_value=1000000, max_value=99999999 ,  required=True)
    fecha_nacimiento = forms.DateField(required=True)
    ocupacion_laboral = forms.CharField(max_length=50, required=True)
    sueldo_mensual = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'dni', 'email', 'telefono',
            'fecha_nacimiento', 'ocupacion_laboral', 'sueldo_mensual'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden. Por favor, intentelo nuevamente.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})