from django.shortcuts import render, redirect
from .forms import categoriaForm
from .models import Categoria
from django.http import JsonResponse
import json
# Create your views here.

def agregar_categoria(request):
    if request.method == "POST":
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver")
    else:
        form = categoriaForm()
    return render(request, "agregar_categoria.html", {"form": form})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    data = [
        {
            "nombre": c.nombre,
            "imagen": c.imagen,
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def ver_categorias(request):
    return render(request, "jsonCategorias.html")

#@csrf_exempt <-- no es seguro hacer esto no lo hagas
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nueva_categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nueva_categoria.id
            },status =201
            )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            },status=400)
    return JsonResponse({
        'error':'Método no es POST'

    },status=405)