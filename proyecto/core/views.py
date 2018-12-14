from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def login(request):
    return render(request, "core/login.html")

def registro(request):
    return render(request, "core/register.html")
