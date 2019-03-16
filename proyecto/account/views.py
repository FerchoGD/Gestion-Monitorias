from django import forms
from .forms import UserCreation
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from perfiles.models.student import Student
from django.views.generic import CreateView
from django.views.generic.base import TemplateView



# Create your views here.
class Login(TemplateView):
    template_name = "account/login.html"


class SignUpView(CreateView):
    form = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

    def get_context_data(self,*args,**kwargs):
        return {'form':self.form}

    def post(self,request,*args,**kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            if len(User.objects.filter(username=request.POST['username'])) == 0:
                user = Student.objects.create(username=request.POST['username'],
                                            name=request.POST['first_name'],
                                            last_name=request.POST['last_name'],
                                            email=request.POST['email'],
                                            birthdate=request.POST['birth_date'],
                                            gender=request.POST['genero'],
                                            subjects = None,
                                            password=request.POST['password1'])
                return redirect("login")
        return render(request, self.template_name, {'form': form,'error':True}) 
