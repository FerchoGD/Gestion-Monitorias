from django.http import HttpResponse
from django.template.loader import get_template
from users.models import User as SystemUser
from core.decorators import UserLogguedDecorator

from django.shortcuts import redirect

@UserLogguedDecorator(type_user='Student')
def view(req, id_student):
    student = SystemUser.objects.filter(pk=id_student)
    if student.count() == 0:
        return redirect('dashboard/student/historial/')
    student = student[0]

    show_alert        = False
    message           = ''
    name_student      = student.user.first_name
    last_name_student = student.user.last_name
    email             = student.user.email
    password1_student = ''
    password2_student = ''
    password3_student = ''

    if req.method == "POST":
        name_student         = req.POST.get("name-student")
        last_name_student    = req.POST.get("last-name-student")
        email                = req.POST.get("email-student").lower()
        password1_student    = req.POST.get("password1-student")
        password2_student    = req.POST.get("password2-student")
        password3_student    = req.POST.get("password3-student")


        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif password2_student != '' and password3_student != '' and  not(DjangoUser.objects.get(email=email).check_password( password1_student )):
            show_alert = True
            message = 'La contraseña actual es incorrecta'
        elif password2_student != password3_student:
            show_alert = True
            message = 'Las nuevas contraseñas no coinciden'
        elif password1_student != '' and password2_student == '' and password3_student == '':
            show_alert = True
            message = 'Debes ingresar ambas contraseñas para actualizar'
        elif email_exists and email != student.user.email:
            show_alert = True
            message = 'El correo ya existe'
        else:
            
            student.user.first_name   = name_student
            student.user.last_name    = last_name_student
            student.user.username     = email
            student.user.email        = email
            student.user.save()

            if(password2_student != '' and password3_student != ''):
                userPass = DjangoUser.objects.get(email=email)
                userPass.set_password(password2_student)
                userPass.save()

            student.save()
            return redirect('/dashboard/student/historial/')

    user = SystemUser.objects.get(user=req.user, type_user='Student')
    image_profile = user.image_profile
    template = get_template('dashboard/students/edit_student.html')

    ctx = {
        'email': email,
        'message': message,
        'show_alert': show_alert,
        'show_students_items': True,
        'name_student': name_student,
        'id_student' : user.pk,
        'image_profile':image_profile,
        'password1_student': password1_student,
        'password2_student': password2_student,
        'password3_student': password3_student,
        'last_name_student': last_name_student,
    }
    return HttpResponse(template.render(ctx, req))
