from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    fecha_nacimiento = forms.DateField(required=False)
    ocupacion_laboral = forms.CharField(max_length=50, required=False)
    sueldo_mensual = forms.DecimalField(max_digits=10, decimal_places=2, required=False)

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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza la presentación de los campos de usuario y contraseña
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})