from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from users.models import User as SystemUser
from subjects.models import Subject

@UserLogguedDecorator(type_user='Admin')
def view(req):
    show_alert              = False
    editting_student        = False
    message                 = ''

    id_student_editting     = 0
    name_student            = ''
    last_name_student       = ''
    dni_student             = ''
    email                   = ''
    password                = ''
    gender                  = ''
    fecha_nacimiento_student= ''

    if req.method == "POST" and 'delete-student' in req.POST:
        id_student = req.POST.get("id_student")
        user = SystemUser.objects.filter(pk=id_student)

        if user.count() != 0:
            user = user[0]
            user.user.delete()

    elif req.method == "POST" and 'create-student-submit' in req.POST:
        name_student = req.POST.get("name-student")
        last_name_student = req.POST.get("last-name-student")
        dni_student = req.POST.get("dni-student")
        email = req.POST.get("email-student").lower()
        password_student = req.POST.get("password-student")
        birth_date = req.POST.get("fecha-nacimiento-student")
        gender = req.POST.get("gender")

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_student).count() != 0

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif email_exists:
            show_alert = True
            message = 'El correo ya existe'
        elif dni_exists:
            show_alert = True
            message = 'El documento ya existe'
        else:
            django_user = DjangoUser(
                username=email,
                first_name=name_student,
                last_name=last_name_student,
                password=password_student,
                email=email
            )
            django_user.save()
            django_user.set_password(password_student)
            django_user.save()

            system_user = SystemUser(
                user=django_user,
                type_user='Student',
                dni=dni_student,
                birth_date=birth_date,
                gender=gender
            )
            system_user.save()

            system_user.save()
    elif req.method == "POST" and 'get-info-student' in req.POST:
        id_student_editting = req.POST.get("id_student")
        user = SystemUser.objects.filter(pk=id_student_editting)

        if user.count() != 0:
            user = user[0]
            name_student        = user.user.first_name
            last_name_student   = user.user.last_name
            dni_student         = user.dni
            email               = user.user.email
            gender                      = user.gender
            fecha_nacimiento_student    = user.birth_date
            editting_student    = True
    elif req.method == "POST" and 'edit-student-submit' in req.POST:
        id_student = req.POST.get("id_student")

        student = SystemUser.objects.get(pk=id_student)

        name_student = req.POST.get("name-student")
        last_name_student = req.POST.get("last-name-student")
        dni_student = req.POST.get("dni-student")
        email = req.POST.get("email-student").lower()
        birth_date = req.POST.get("fecha-nacimiento-student")
        gender = req.POST.get("gender")

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_student).count() != 0

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif email_exists and email != student.user.email:
            show_alert = True
            message = 'El correo ya existe'
        elif dni_exists and dni_student != student.dni:
            show_alert = True
            message = 'El documento ya existe'
        else:
            student.user.username=email
            student.user.first_name=name_student
            student.user.last_name=last_name_student
            student.user.email=email
            student.user.save()

            student.dni=dni_student
            student.birth_date=birth_date
            student.gender=gender
            student.save()

            student.save()

    students = SystemUser.objects.filter(type_user='Student')
    
    genders = ['Masculino','Femenino']

    user = SystemUser.objects.get(user=req.user, type_user='Admin')
    image_profile = user.image_profile

    template = get_template('dashboard/admins/students.html')
    ctx = {
        'show_alert': show_alert,
        'email': email,
        'genero':gender,
        'genders':genders,
        'message': message,
        'id_admin': user.pk,
        'students': students,
        'show_admins_items': True,
        'dni_student': dni_student,
        'name_student': name_student,
        'image_profile':image_profile,
        'editting_student': editting_student,
        'last_name_student': last_name_student,
        'id_student_editting': id_student_editting,
        'fecha_nacimiento_student':fecha_nacimiento_student
    }
    return HttpResponse(template.render(ctx, req))
