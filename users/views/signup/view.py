from django.http import HttpResponse
from django.template.loader import get_template

from users.models import User as SystemUser
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def view(req):
    show_alert = True
    message = 'El registro solo se realiza para estudiantes'
    name_student             = ''
    last_name_student        = ''
    dni_student              = ''
    email_student            = ''
    password1_student        = ''
    password2_student        = ''
    gender                   = ''
    fecha_nacimiento_student = ''

    if req.method == "POST":
        name_student         = req.POST.get("name-student")
        last_name_student    = req.POST.get("last-name-student")
        dni_student          = req.POST.get("dni-student")
        email_student        = req.POST.get("email-student").lower()
        password1_student    = req.POST.get("password1-student")
        password2_student    = req.POST.get("password2-student")
        birth_date           = req.POST.get("fecha-nacimiento-student")
        gender               = req.POST.get("gender")


        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email_student.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email_student).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_student).count() != 0
        

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif password1_student != password2_student:
            show_alert = True
            message = 'las contraseñas no coinciden'
        elif email_exists:
            show_alert = True
            message = 'El correo ya existe'
        elif dni_exists:
            show_alert = True
            message = 'El documento de identidad ya existe'
        else:

            django_user = DjangoUser(
                username=email_student,
                first_name=name_student,
                last_name=last_name_student,
                email=email_student
            )
            django_user.save()
            django_user.set_password(password1_student)
            django_user.save()

            system_user = SystemUser(
                user=django_user,
                type_user='Student',
                dni=dni_student,
                birth_date=birth_date,
                gender=gender
            )
            system_user.save()
            return redirect('/login/')

    genders = ['Masculino','Femenino']
    template = get_template('signup/signup.html')

    ctx = {
        'show_Alert': show_alert,
        'message': message,
        'Inicio': False,
        'name_student': name_student,
        'last_name_student': last_name_student,
        'dni_student': dni_student,
        'fecha_nacimiento_student':fecha_nacimiento_student,
        'genders':genders,
        'gender':gender,
        'email_student': email_student,
        'password1_student': password1_student,
        'password2_student': password2_student,
    }

    return HttpResponse(template.render(ctx, req))
