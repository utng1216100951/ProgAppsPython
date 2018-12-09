from django.shortcuts import render
#django library
from django.views.generic import (
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    # que una vista procesa los datos y renderiza el rsultado en pantalla
    # siempre nos pedira un template con el que trabajar
    # un template es un archivo html
    template_name = "home/index.html"


class ListaLibros(ListView):
    template_name = 'home/lista.html'
    queryset = ['El quijote de la mancha', 'Codigo Limpio', 'La sombra del viento', 'Django 2.0']
    context_object_name = 'libros'
