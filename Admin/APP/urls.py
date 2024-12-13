from django.urls import path
from APP import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),
    path('about/', views.about, name='about'),
]
