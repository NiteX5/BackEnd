from django.shortcuts import render

# Create your views here.
def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarCotisacion(request):
    return render(request, 'cotisacion.html')

def mostrarDetalles(request):
    return render(request, 'detalles.html')