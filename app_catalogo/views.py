# app_catalogo/views.py
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .datos import LIBROS, buscar_libro



def inicio(request):
    
    disponibles = sum(1 for libro in LIBROS if libro["disponible"])
    prestados = len(LIBROS) - disponibles

    contexto = {
        "nombre_sitio": "Catálogo ADSO",
        "total": len(LIBROS),
        "disponibles": disponibles,
        "prestados": prestados,
    }
    return render(request, "app_catalogo/inicio.html", contexto)


def lista_libros(request):
    genero = request.GET.get("genero", "")
    if genero:
        libros = [libro for libro in LIBROS if libro["genero"] == genero]
    else:
        libros = LIBROS
    return render(request, "app_catalogo/lista.html", {"libros": libros, "genero": genero})


def detalle_libro(request, libro_id):
    libro = buscar_libro(libro_id)
    if libro is None:
        raise Http404("El libro no existe")
    return render(request, "app_catalogo/detalle.html", {"libro": libro})


class AcercaView(TemplateView):
    template_name = "app_catalogo/acerca.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["version"] = "1.0"
        return contexto



def hola(request):
    return HttpResponse("Hola desde Django")



def cuadrado(request, numero):
    return HttpResponse(f"El cuadrado de {numero} es {numero ** 2}")




class ContactoView(TemplateView):
    template_name = "app_catalogo/contacto.html"



def autores(request):
    conteo = {}
    for libro in LIBROS:
        autor = libro["autor"]
        conteo[autor] = conteo.get(autor, 0) + 1

    lista_autores = sorted(conteo.items())

    return render(request, "app_catalogo/autores.html", {"autores": lista_autores})



def sugerir(request):
    titulo = ""
    mensaje = ""

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        if titulo:
            mensaje = f"Gracias, tendremos en cuenta: {titulo}"
        else:
            mensaje = "Escribe un título"

    return render(request, "app_catalogo/sugerir.html", {"mensaje": mensaje, "titulo": titulo})



def ordenados(request, campo):
    campos_validos = ("titulo", "anio", "autor")

    if campo not in campos_validos:
        raise Http404(f"Orden no válido: {campo}")

    libros = sorted(LIBROS, key=lambda l: l[campo])

    return render(
        request,
        "app_catalogo/ordenados.html",
        {"libros": libros, "campo": campo},
    )