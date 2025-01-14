from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h2>Hello Unhappy</h2>')

def user(request):
    return render(request, 'user.html', status=200)

def show_error404(request):
    return render(request, '404.html', status=404)

def show_error500(request):
    return render(request, '500.html', status=500)

def generar_error(request):
    return 1/0