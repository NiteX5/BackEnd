from django.shortcuts import render

# Create your views here.
def mostrarFormulario(request):
    return render(request, 'formulario.html')