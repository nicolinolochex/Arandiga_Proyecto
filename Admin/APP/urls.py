from django.urls import path
from APP import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('formulario/', views.formulario),
    path('about/', views.about),
    path('BKP/', views.about)
]
