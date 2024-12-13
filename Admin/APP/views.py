from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Contact

def inicio(request):
    return render(request, "APP/inicio.html")

def formulario(request):
    if request.method == 'POST':
        # Obtenemos los datos enviados en el formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Creamos una instancia del modelo y guardamos los datos
        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        # Redirigimos a una página de éxito o mostramos un mensaje
        return render(request, "APP/success.html")  # Asegúrate de crear success.html
    return render(request, "APP/formulario.html")

def about(request):
    return render(request,"APP/about.html")

def about(request):
    return render(request,"APP/BKP.html")