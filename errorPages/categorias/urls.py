from django.urls import path
from .views import *

urlpatterns = [
    path("agregar/", agregar_categoria, name="agregar"),
    path("ver/", ver_categorias, name="ver"),
    path("api/get/", listar_categorias, name="lista"),
    path('api/post/',registrar_categoria,name='post'),
]
