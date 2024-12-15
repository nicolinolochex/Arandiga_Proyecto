from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import VehiculosClientesForm
from .forms import TrabajaConNosotrosForm


def inicio(request):
    return render(request, "APP/inicio.html")



def formulario(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            form.save()
            # Redirigir a una página de éxito o mostrar un mensaje
            return redirect('success')  # Redirige a una vista de éxito, por ejemplo
    else:
        form = ContactForm()

    return render(request, 'app/formulario.html', {'form': form})

def success(request):
    return render(request, 'APP/success.html')

def about(request):
    return render(request,"APP/aboutv2.html")

def base_clientes(request):
    return render(request,"APP/base_clientes.html")

def publicar_rodado(request):
    if request.method == 'POST':
        form = VehiculosClientesForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            form.save()
            # Redirigir a una página de éxito
            return redirect('success')  # Redirige a una vista de éxito, por ejemplo
    else:
        form = VehiculosClientesForm()

    return render(request, 'APP/publicar_rodado.html', {'form': form})

def publicar_cv(request):
    if request.method == 'POST':
        form = TrabajaConNosotrosForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            form.save()
            # Redirigir a una página de éxito
            return redirect('success')  # Redirige a una vista de éxito, por ejemplo
    else:
        form = TrabajaConNosotrosForm()

    return render(request, 'APP/publicar_cv.html', {'form': form})


