from django.urls import path
from APP import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),  # Asegúrate de que la vista formulario esté apuntando al formulario correcto
    path('acercade/', views.about, name='aboutv2'),
    path('base_clientes/', views.base_clientes, name='base_clientes'),
    path('publica/', views.publica, name='publica'),
    path('trabaja/', views.trabaja, name='trabaja'),
    path('success/', views.success, name='success'),  # Esta es la URL para success

]
