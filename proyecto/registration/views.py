from .forms import UserCreation
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        CHOICES = [('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro')]
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo real
        form.fields['identificacion'].widget = forms.TextInput(attrs={'class':'form-control mb-2', ' placeholder': 'ID'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', ' placeholder': 'Nombres'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', ' placeholder': 'Apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', ' placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.TextInput(attrs={'class':'form-control mb-2', ' placeholder': 'Correo'})
        form.fields['genero'].widget = forms.Select(attrs={'class':'form-control mb-2', ' placeholder': 'Genero'}, choices=CHOICES)
        form.fields['birth_date'].widget = forms.DateInput(attrs={'class':'form-control mb-2', ' placeholder': 'Fecha Nacimiento'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', ' placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', ' placeholder': 'Confirmar contraseña'})
        return form