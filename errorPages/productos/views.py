from django.shortcuts import render, redirect

# Create your views here.
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse

#Agregar un nuevo producto
def agregar_producto(request):
    if request.method == "POST":
        form = productoForm(request.POST) #Se crea un formulario lleno con la información que se envió
        if form.is_valid():
            form.save()
            return redirect("ver") #Redirigir a la página de inicio
    else:
        form = productoForm()
    return render(request, "agregar_producto.html", {"form": form})

#Mostrar todos los productos
def ver_productos(request):
    productos = Producto.objects.all() #Obtener todos los productos
    return render(request, "ver.html", {"productos": productos})


#Devuelve el JSON
def list_produdctos(request):
    productos = Producto.objects.all()
    #Para enviar un JSON se debe escribir en un diccionario usando llaves
    data = [
        {
            "nombre": p.nombre,
            "precio": p.precio,
            "imagen": p.imagen,
        }
        for p in productos
    ]
    return JsonResponse(data, safe=False)

def ver_jsonData(request):
    return render(request, "json.html")