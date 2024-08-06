from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30) #esto genera un texto
    comision = models.IntegerField() #esto genera un entero
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    profesor = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesor = models.CharField(max_length=40)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField ()
    entregado = models.BooleanField() #si o no
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)




