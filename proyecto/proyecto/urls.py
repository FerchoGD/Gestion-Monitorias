"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registration.views import SignUpView
from perfiles.views import superusuario
from core.views import home, registro, registro_estudiante, registro_monitor



urlpatterns = [
    path('', home.as_view(), name="home"),
    
    path('register-estud/', registro_estudiante.as_view(), name="register-est"),
    path('register-monit/', registro_monitor.as_view(), name="register-mon"),
    

    #Paths de perfiles
    
    path('index-su/', superusuario.as_view(), name="superu"),
    #path('index-adm/', administrador.as_view(), name="admin"),
    #path('index-est/', estudiante.as_view(), name="est"),
    #path('index-mon/', monitor.as_view(), name="mon"),
    
    #Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    path('admin/', admin.site.urls),

]
