from django.db import models

# Aqui se importan los modelos de django a la base de datos
# Se puede hacer a la inversa tambien

class ErrorLog(models.Model):
    #Es el equivalente a poner un varchar
    codigo = models.CharField(max_length=10)
    #Es el equivalente a poner un logText
    mensaje = models.TextField()
    #Es el equivalente a poner un Date(now())
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.codigo} - {self.mensaje}"
