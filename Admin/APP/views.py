from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import VehiculosClientesForm
from .forms import TrabajaConNosotrosForm
from .forms import BuscaVehiculoForm
from .models import VehiculosClientes


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

def tests(request):
    return render(request, 'APP/tests.html')

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

def buscar_vehiculo(request):
    vehiculos = []  # Lista para almacenar los vehículos que coincidan con la búsqueda
    if request.method == "POST":
        mi_formulario = BuscaVehiculoForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            # Filtramos los vehículos por unidad o modelo
            vehiculos = VehiculosClientes.objects.filter(
                unidad__icontains=informacion["unidad"],
                modelo__icontains=informacion["modelo"]
            )
    else:
        mi_formulario = BuscaVehiculoForm()

    return render(request, "APP/buscar_vehiculo.html", {
        "mi_formulario": mi_formulario,
        "vehiculos": vehiculos  # Pasamos los vehículos filtrados o vacíos
    })
