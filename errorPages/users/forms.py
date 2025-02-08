from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
import re


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control col-6",
                "placeholder": "Ent er your password",
                "required": True,
            }
        ),
        help_text="<ul><li>Password must contain at least 8 characters.</li><li>Password cannot be similar to other personal information.</li><li>Password cannot be a common password.</li></ul>",
        label="Password",
    ) 
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control col-6 mb-4",
                "placeholder": "Ingrese de nuevo su contraseña",
                "required": True,
            }
        ),
        label="Confirm password",
    ) 

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
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control col-6",
                    "placeholder": "Ingrese su correo electrónico",
                    "required": True,
                    "pattern": r"^[0-9]{5}[a-z,A-Z]{2}[0-9]{3}@utez\.edu\.mx$",
                    "title": "El correo electrónico debe tener el formato 12345ab678@utez.edu.mx",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control col-6",
                    "placeholder": "Ingrese su nombre",
                    "required": True,
                }
            ),
            "surname": forms.TextInput(
                attrs={
                    "class": "form-control col-6",
                    "placeholder": "Ingrese su apellido",
                    "required": True,
                }
            ),
            "control_number": forms.TextInput(
                attrs={
                    "class": "form-control col-6",
                    "placeholder": "Ingrese su número de control",
                    "required": True,
                    "pattern": r"^[0-9]{5}[a-z,A-Z]{2}[0-9]{3}$",
                    "title": "El número de control debe tener el formato 12345ab678",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control col-6",
                    "placeholder": "Ingrese su edad",
                    "required": True,
                }
            ),
            "tel": forms.TextInput(
                attrs={
                    "class": "form-control col-6",
                    "placeholder": "Ingrese su número de teléfono",
                    "required": True,
                    "pattern": r"^[0-9]{10}$",
                    "title": "El número de teléfono debe tener 10 dígitos",
                }
            ),
        }
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        name = cleaned_data.get('name')
        surname = cleaned_data.get('surname')
        control_number = cleaned_data.get('control_number')
        age = cleaned_data.get('age')
        tel = cleaned_data.get('tel')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if len(name) > 30:
            raise forms.ValidationError({'name': 'El nombre no puede tener más de 30 caracteres.'})
        
        if len(surname) > 30:
            raise forms.ValidationError({'surname': 'El apellido no puede tener más de 30 caracteres.'})
        
        if len(control_number) > 10:
            raise forms.ValidationError({'control_number': 'El número de control no puede tener más de 15 caracteres.'})
        
        if age < 1 or age > 120:
            raise forms.ValidationError({'age': 'La edad debe estar entre 1 y 120 años.'})
        
        if len(tel) > 10 or len(tel) < 10:
            raise forms.ValidationError({'tel': 'El teléfono debe tener exactamente 10 digitos.'})
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError({'password2': 'Las contraseñas no coinciden.'})


        if not email.endswith('@utez.edu.mx'):
            raise forms.ValidationError({'email': 'El correo debe ser de la UTEZ (@utez.edu.mx).'})

        if not re.match(r'^[0-9]{4}[1-3]{1}[a-zA-Z]{2}[0-9]{3}$', control_number):
            raise forms.ValidationError({'control_number': 'La matrícula debe ser de la UTEZ (ejemplo: 20223tn052).'})

        if not re.match(r'^\d{10}$', tel):
            raise forms.ValidationError({'tel': 'El teléfono debe tener exactamente 10 dígitos.'})

        if password1 != password2:
            raise forms.ValidationError({'password2': 'Las contraseñas no coinciden.'})
        
        if password2 != password1:
            raise forms.ValidationError({'password1': 'Las contraseñas no coinciden.'})

        if not re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
            raise forms.ValidationError({'password1': 'La contraseña debe tener al menos 8 caracteres, 1 número, 1 letra mayúscula y 1 carácter especial.'})

        return cleaned_data


class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control col-2",
                "placeholder": "Ingrese su correo electrónico",
                "required": True,
                "pattern": r"^[0-9]{5}[a-z,A-Z]{2}[0-9]{3}@utez\.edu\.mx$",
                "title": "El correo electrónico debe tener el formato",
            } ),
        label = "Email",
        
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control col-2 text-white",
                "placeholder": "Ingrese su contraseña",
                "required": True,
            }
        ),
        label="Password",
    )  

    pass
