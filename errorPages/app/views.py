from django.shortcuts import render
from django.http import HttpResponse
from .utils import google_search


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

def onepage(request):
    return render(request, 'onePage.html', status=200)

def busqueda(request):
    query = request.GET.get("q","")
    results = []
    if query:
        data = google_search(query)
        results = data.get('items', [])
    return render(request, 'search.html', {'results': results, 'query': query})