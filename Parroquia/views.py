from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import	Video, Donacion

# Create your views here.

def index(request):
	return render(request, 'index.html')

def info(request):
	return render(request, 'info.html')

def documentos(request):
	return render(request, 'documentos.html')

def galeria(request):
	videos = Video.objects.all()
	return render(request, 'galeria.html', {'videos' : videos})

def donacion(request):
	donaciones = Donacion.objects.all()
	return render(request, 'donacion.html', {'donaciones' : donaciones})