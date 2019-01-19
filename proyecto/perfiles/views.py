from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class superusuario(TemplateView):
    template_name = "perfiles/index_su.html"

class monitor(TemplateView):
    template_name = "perfiles/index_monitor.html"

class estudiante(TemplateView):
    template_name = "perfiles/index_estudiante.html"

class administrador(TemplateView):
    template_name = "perfiles/index_admin.html"