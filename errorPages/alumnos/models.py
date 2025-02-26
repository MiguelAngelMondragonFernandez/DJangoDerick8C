from django.db import models

# Create your models here.
class Alumno(models.Model):
    #Definir los atributos de clase
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(max_length=100,unique=True)
    matricula = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre