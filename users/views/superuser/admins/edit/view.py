from django.http import HttpResponse
from django.template.loader import get_template
from users.models import User as SystemUser
from core.decorators import UserLogguedDecorator

from django.shortcuts import redirect

@UserLogguedDecorator()
def view(req, id_admin):
    admin = SystemUser.objects.filter(pk=id_admin)
    if admin.count() == 0:
        return redirect('/dashboard/superuser/')
    admin = admin[0]

    show_alert      = False
    message         = ''
    name_admin      = admin.user.first_name
    last_name_admin = admin.user.last_name
    dni_admin       = admin.dni
    email           = admin.user.email
    password        = ''

    if req.method == "POST":
        name_admin         = req.POST.get("name-admin")
        last_name_admin    = req.POST.get("last-name-admin")
        dni_admin          = req.POST.get("dni-admin")
        email              = req.POST.get("email-admin").lower()

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_admin).count() != 0

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif email_exists and email != admin.user.email:
            show_alert = True
            message = 'El correo ya existe'
        elif dni_exists and dni_admin != admin.dni:
            show_alert = True
            message = 'El documento ya existe'
        else:
            admin.user.first_name   = name_admin
            admin.user.last_name    = last_name_admin
            admin.user.username     = email
            admin.user.email        = email
            admin.user.save()

            admin.dni = dni_admin
            admin.save()

            return redirect('/dashboard/superuser/')

    user = SystemUser.objects.get(user=req.user)
    image_profile = user.image_profile
    template = get_template('dashboard/edit_admin.html')
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
