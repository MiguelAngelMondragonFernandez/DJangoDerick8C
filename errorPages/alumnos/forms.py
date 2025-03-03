# filepath: /c:/Users/mickV/OneDrive/Desktop/DJangoDerick8C/errorPages/alumnos/forms.py
from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'edad', 'email', 'matricula', 'apellido']

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del alumno",
                    "id": "nombre",
                }
            ),
            "edad": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la edad del alumno",
                    "id": "edad",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el email del alumno",
                    "id": "email",
                }),
                "matricula": forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Ingrese la matricula del alumno",
                        "id": "matricula",
                    }
                ),
                "apellido": forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Ingrese el apellido del alumno",
                        "id": "apellido",
                    }
                ),


        }

        labels = {
            "nombre": "Nombre del alumno",
            "edad": "Edad",
            "email": "Correo electrónico",
        }

        error_messages = {
            "nombre": {
                "required": "El nombre del alumno es obligatorio",
            },
            "edad": {
                "required": "La edad no puede estar vacía",
                "invalid": "Ingrese un número válido",
            },
            "email": {
                "required": "El correo electrónico es obligatorio",
                "invalid": "Ingrese un correo electrónico válido",
            },
        }