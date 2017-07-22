from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import	User

@python_2_unicode_compatible
class Video(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=15)
	
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Album(models.Model):
	nombre = models.CharField(max_length=35)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Imagen(models.Model):
	nombre = models.CharField(max_length=30)
	foto = models.FileField(upload_to="images")
	
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Donacion(models.Model):
	banco = models.CharField(max_length=30)
	cuenta = models.CharField(max_length=15)
	
	def __str__(self):
		return self.banco		