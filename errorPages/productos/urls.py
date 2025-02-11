from django.urls import path
from .views import *

urlpatterns = [
    path("agregar/", agregar_producto, name="agregar"),
    path("ver/", ver_productos, name="ver"),
    path("api/get/", list_produdctos, name="lista"),
    path("json/", ver_jsonData, name="json"),
]