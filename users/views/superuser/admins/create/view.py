from django.http import HttpResponse
from django.template.loader import get_template
from users.models import User as SystemUser
from core.decorators import UserLogguedDecorator

from django.shortcuts import redirect

@UserLogguedDecorator()
def view(req):
    show_alert      = False
    message         = ''
    name_admin      = ''
    last_name_admin = ''
    dni_admin       = ''
    email           = ''
    password        = ''

    if req.method == "POST":
        name_admin         = req.POST.get("name-admin")
        last_name_admin    = req.POST.get("last-name-admin")
        dni_admin          = req.POST.get("dni-admin")
        email              = req.POST.get("email-admin").lower()
        password_user      = req.POST.get("password-admin")

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_admin).count() != 0

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
            user = DjangoUser(
                username=email,
                email=email,
                first_name=name_admin,
                last_name=last_name_admin,
                password=password_user
            )
            user.save()
            user.set_password(password_user)
            user.save()
            system_user = SystemUser(
                user=user,
                type_user='Admin',
                dni=dni_admin
            )
            system_user.save()

            return redirect('/dashboard/superuser/')

    user = SystemUser.objects.get(user=req.user)
    image_profile = user.image_profile

    template = get_template('dashboard/create_admin.html')
    ctx = {
        'email': email,
        'message': message,
        'password': password,
        'dni_admin': dni_admin,
        'show_alert': show_alert,
        'name_admin': name_admin,
        'show_superuser_items': True,
        'image_profile':image_profile,
        'last_name_admin': last_name_admin

    }
    return HttpResponse(template.render(ctx, req))
