from django.db import models

class Alumno(models.Model):
	nombre = models.CharField('Nombre del alumno',max_length=60)
	apellido = models.CharField(max_length=60)
	edad = models.IntegerField(blank=False)
	calificacion = models.FloatField(blank=False)

	def __str__(self):
		return str(self.nombre)+" "+str(self.apellido)

# Create your models here.
