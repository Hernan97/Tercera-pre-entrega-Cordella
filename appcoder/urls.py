from django.urls import path

from appcoder.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('precios/', precios, name="precios"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('crearcurso/', crearcurso, name="crearcurso"),
    path('crearestudiante/', crearestudiante, name="crearestudiante"),
]




