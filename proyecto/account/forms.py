from django import forms
from django.contrib.auth.models import User
import datetime

class UserCreation(forms.Form):
    CHOICES = [('Hombre', 'Hombre'), ('Mujer', 'Mujer'), ('Otro', 'Otro')]
    username = forms.CharField(label="Username",max_length=250,required=True)
    genero = forms.ChoiceField(choices=CHOICES)
    identificacion = forms.IntegerField(required=True)
    birth_date = forms.DateField(required=True,initial=datetime.date.today)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True, help_text="Requerido")
    password1 = forms.CharField(max_length=250, required=True)
    password2 = forms.CharField(max_length=250, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email", "birth_date", "genero", "identificacion", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        base, exten = email.split("@")
        if not "utp.edu.co" == exten:
            raise forms.ValidationError("Ingrese por favor el correo institucional")
        return email