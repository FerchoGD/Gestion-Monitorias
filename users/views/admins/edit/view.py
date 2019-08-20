from django.http import HttpResponse
from django.template.loader import get_template
from users.models import User as SystemUser
from core.decorators import UserLogguedDecorator

from django.shortcuts import redirect

@UserLogguedDecorator(type_user='Admin')
def view(req, id_admin):
    admin = SystemUser.objects.filter(pk=id_admin)
    if admin.count() == 0:
        return redirect('/dashboard/admin/')
    admin = admin[0]

    show_alert      = False
    message         = ''
    name_admin      = admin.user.first_name
    last_name_admin = admin.user.last_name
    dni_admin       = admin.dni
    email           = admin.user.email
    password1_admin = ''
    password2_admin = ''
    password3_admin = ''

    if req.method == "POST":
        name_admin         = req.POST.get("name-admin")
        last_name_admin    = req.POST.get("last-name-admin")
        dni_admin          = req.POST.get("dni-admin")
        email              = req.POST.get("email-admin").lower()
        password1_admin    = req.POST.get("password1-admin")
        password2_admin    = req.POST.get("password2-admin")
        password3_admin    = req.POST.get("password3-admin")

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_admin).count() != 0

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif password2_admin != '' and password3_admin != '' and not(DjangoUser.objects.get(email=email).check_password( password1_admin )):
            show_alert = True
            message = 'La contraseña actual es incorrecta'
        elif password2_admin != password3_admin:
            show_alert = True
            message = 'Las nuevas contraseñas no coinciden'
        elif password1_admin != '' and password2_admin == '' and password3_admin == '':
            show_alert = True
            message = 'Debes ingresar ambas contraseñas para actualizar'
        elif email_exists and email != admin.user.email:
            show_alert = True
            message = 'El correo ya existe'
        elif dni_exists and dni_admin != admin.dni:
            show_alert = True
            message = 'El documento ya existe'
        else:
            admin.image_profile = req.FILES.get('image')
            admin.user.first_name   = name_admin
            admin.user.last_name    = last_name_admin
            admin.user.username     = email
            admin.user.email        = email
            admin.user.save()

            if(password2_admin != '' and password3_admin != ''):
                userPass = DjangoUser.objects.get(email=email)
                userPass.set_password(password2_admin)
                userPass.save()
            
            admin.dni = dni_admin
            admin.save()

            return redirect('/dashboard/admin/')

    user = SystemUser.objects.get(user=req.user, type_user='Admin')
    image_profile = user.image_profile

    template = get_template('dashboard/edit_admin.html')
    ctx = {
        'show_alert': show_alert,
        'message': message,
        'show_admins_items': True,
        'name_admin': name_admin,
        'last_name_admin': last_name_admin,
        'dni_admin': dni_admin,
        'email': email,
        'id_admin': id_admin,
        'image_profile':image_profile,
        'password1_admin':password1_admin,
        'password2_admin':password2_admin,
        'password3_admin':password3_admin
    }
    return HttpResponse(template.render(ctx, req))
