from django.urls import path
from APP import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),  # Asegúrate de que la vista formulario esté apuntando al formulario correcto
    path('acercade/', views.about, name='aboutv2'),
    path('base_clientes/', views.base_clientes, name='base_clientes'),
    path('publicar_cv/', views.publicar_cv, name='publicar_cv'),
    path('publicar_rodado/', views.publicar_rodado, name='publicar_rodado'),
    path('success/', views.success, name='success'),  # Esta es la URL para success

]
