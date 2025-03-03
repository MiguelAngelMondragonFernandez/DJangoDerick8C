from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from .forms import AlumnoForm

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]
    #http_method_names = ['get', 'post', 'put', 'delete'] Limitar los métodos HTTP que se pueden usar



def agregar_alumno(request):
    form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})