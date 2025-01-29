from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "name",
            "surname",
            "control_number",
            "age",
            "tel",
            "password1",
            "password2",
        ]

        widget = {
            "email": forms.EmailField(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese su correo electronico",
                    "required": True,
                    "pattern": "^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "require": True,
                    "class": "form-control",
                    "placeholder": "Ingrese su nombre completo",
                }
            ),
        }


class CustomUserLoginForm(AuthenticationForm):
    pass
