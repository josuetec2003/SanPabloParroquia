from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^galeria/$', views.galeria, name='galeria'),
	url(r'^donacion/$', views.donacion, name='donacion'),
	url(r'^info/$', views.info, name='info'),
	url(r'^documentos/$', views.documentos, name='documentos'),

]