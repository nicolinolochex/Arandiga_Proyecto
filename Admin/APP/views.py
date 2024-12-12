from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "APP/inicio.html")

def formulario(request):
    return render(request,"APP/formulario.html")

def about(request):
    return render(request,"APP/about.html")

def about(request):
    return render(request,"APP/BKP.html")