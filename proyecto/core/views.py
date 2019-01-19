from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class home(TemplateView):
    template_name = "core/home.html"

class registro(TemplateView):
    template_name = "core/register.html"

class registro_estudiante(TemplateView):
    template_name = "core/register_estudiante.html"

class registro_monitor(TemplateView):
    template_name = "core/register_monitor.html"
