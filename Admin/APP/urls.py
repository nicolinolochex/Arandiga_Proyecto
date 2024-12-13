from django.urls import path
from APP import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),
    path('acercade/', views.about, name='aboutv2'),
]
