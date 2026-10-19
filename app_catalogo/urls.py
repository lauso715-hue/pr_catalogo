
# app_catalogo/urls.py
from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    path("libros/", views.lista_libros, name="lista_libros"),
    path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
    path("acerca/", views.AcercaView.as_view(), name="acerca"),

    # ejercicios generales
    path("hola/", views.hola, name="hola"),
    path("cuadrado/<int:numero>/", views.cuadrado, name="cuadrado"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),
    path("autores/", views.autores, name="autores"),
    path("sugerir/", views.sugerir, name="sugerir"),

    # ejercicio individual
    path("libros/orden/<str:campo>/", views.ordenados, name="ordenados"),
]