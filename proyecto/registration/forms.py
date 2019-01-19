from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreation(UserCreationForm):
    CHOICES = [('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro')]
    genero = forms.ChoiceField(choices=CHOICES)
    identificacion = forms.IntegerField(required=True)
    birth_date = forms.DateField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True, help_text="Requerido")

    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email", "birth_date", "genero", "identificacion", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        base, exten = email.split("@")
        if not "utp.edu.co" == exten:
            raise forms.ValidationError("Ingrese por favor el correo institucional")
        return email