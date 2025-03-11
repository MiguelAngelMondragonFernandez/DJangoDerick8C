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

       # widgets: {
            #'email': forms.EmailField(
            
            #    attrs={
             #       'class': 'form-control',
            #        'placeholder': 'Ingrese su correo',
           #         'required': True,
          #          'pattern': '^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$',
         #       }
        #    ),
       #     'name': forms.TextInput(
      #          attrs={
     #               'class': 'form-control',
    #                'placeholder': 'Ingrese su nombre completo',
   #                 'required': True,
  #              }
 #           )
#        }


class CustomUserLoginForm(AuthenticationForm):
    pass
