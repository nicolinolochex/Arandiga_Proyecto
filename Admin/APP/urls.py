from django.urls import path
from APP import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),
    path('acercade/', views.about, name='aboutv2'),
    path('base_clientes/', views.base_clientes, name='base_clientes')
]
