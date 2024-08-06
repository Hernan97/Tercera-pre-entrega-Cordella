from django.shortcuts import render

from django.http import HttpResponse

from .models import Curso, Estudiante
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def precios(request):
    return render(request, "appcoder/precios.html")

def estudiantes(request):
    return HttpResponse("Bienvenido a la página de estudiantes")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
        cursos = Curso.objects.all() # Muestra todos los cursos si no se proporciona un nombre
        nombre_curso = request.GET.get('nombre', '').strip()  # Obtiene el parámetro de búsqueda
        cursos =[]
        if nombre_curso:
            cursos = Curso.objects.filter(nombre__icontains=nombre_curso)  # Filtra los cursos por nombre
        else:
            cursos = Curso.objects.all()  # Muestra todos los cursos si no se proporciona un nombre
            no_courses_found = nombre_curso and not cursos
        estudiantes = Estudiante.objects.all()
        nombre_estudiante = request.GET.get('nombre', '').strip()  # Obtiene el parámetro de búsqueda
        estudiantes =[]
        if nombre_estudiante:
            estudiantes = Estudiante.objects.filter(nombre__icontains=nombre_estudiante)  # Filtra los estudiantes por nombre
        else:
            estudiantes = Estudiante.objects.all()  # Muestra todos los estudiantes si no se proporciona un nombre
            no_students_found = nombre_estudiante and not estudiantes
        contexto = {"cursos": cursos }
        contexto.update ({"estudiantes": estudiantes })
        contexto.update ({"no_courses_found": no_courses_found})
        contexto.update ({"no_students_found": no_students_found})
        return render(request, "appcoder/entregables.html", contexto)

def crearcurso(request):
    texto = None
    if 'nombre_curso' in request.GET and 'comision_curso' in request.GET:
        nombre_curso = request.GET.get('nombre_curso')
        comision_curso = request.GET.get('comision_curso')
        
        if nombre_curso and comision_curso:
            try:
                comision_curso = int(comision_curso)  # Convertir a entero
                curso = Curso(nombre=nombre_curso, comision=comision_curso)
                curso.save()
                texto = "Curso registrado con éxito"
            except ValueError:
                texto = "El número de comisión debe ser un número entero."
        else:
            texto = "Por favor, complete todos los campos."
    return render(request, "appcoder/crearcurso.html", {"texto": texto})

def crearestudiante(request):
    mensaje = None
    if "nombre_estudiante" in request.GET and "apellido_estudiante" in request.GET:
        nombre_estudiante = request.GET.get('nombre_estudiante')
        apellido_estudiante = request.GET.get('apellido_estudiante')
        email_estudiante = request.GET.get('email_estudiante')
        if nombre_estudiante and apellido_estudiante and email_estudiante:
            # Valida el formato del email si es necesario
            estudiante = Estudiante(nombre=nombre_estudiante, apellido=apellido_estudiante, email=email_estudiante)
            try:
                estudiante.save()
                mensaje = "Estudiante registrado con éxito"
            except Exception as e:
                mensaje = f"Error al registrar el estudiante: {e}"
        else:
            mensaje = "Por favor, complete todos los campos."
    return render(request, "appcoder/crearestudiante.html", {"mensaje": mensaje}) 


class CursoDetailView(DetailView):
    model= Curso
    template_name= "appcoder/entregables.html"

class CursoListView(ListView): #mostrar una lista, listar objetos
    model = Curso  #sobre que objeto vamos a trabajar
    context_object_name="cursos" #nombre con el cual le va a llegar al template
    template_name= "appcoder/entregables.html"   #template donde va a plasmar los datos

class CursoCreateView(CreateView): #crear objetos de una lista
    model = Curso  #sobre que objeto vamos a trabajar
    template_name= "appcoder/entregables.html"   #template donde va a plasmar los datos
    success_url = reverse_lazy ("entregables")
    fields = ["nombre","comision"]

