from django import forms
from .models import Producto

#Se puede crear un formulario para cada modelo que exista

class productoForm (forms.ModelForm):
    class Meta:
        #Definir de que modelo se va a crear el formulario
        model = Producto
        #Definir que campos se van a mostrar en el formulario
        fields = ['nombre', 'precio', 'imagen']


        #Definir como se deben de mostrar los campos
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el nombre del producto",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese el precio del producto",
                }
            ),
            "imagen": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingrese la URL de la imagen del producto",
                }
            ),
        }

        labels = {
            "nombre": "Nombre del producto",
            "precio": "Moneda nacional",
            "imagen": "URL de la imagen del producto",
        }


        #Mensajes de error personalizados
        error_messages = {
            "nombre": {
                "required": "El nombre del producto es obligatorio",
            },
            "precio": {
                "required": "El precio no puede estar vacío",
                "invalid": "Ingrese un número válido",
            },
            "imagen": {
                "required": "La URL de la imagen del producto es requerida",
            },
        }