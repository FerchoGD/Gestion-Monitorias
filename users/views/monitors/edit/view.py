from django.http import HttpResponse
from django.template.loader import get_template
from users.models import User as SystemUser
from core.decorators import UserLogguedDecorator

from django.shortcuts import redirect

@UserLogguedDecorator(type_user='Monitor')
def view(req, id_monitor):
    monitor = SystemUser.objects.filter(pk=id_monitor)
    if monitor.count() == 0:
        return redirect('/dashboard/monitor/')
    monitor = monitor[0]

    show_alert        = False
    message           = ''
    name_monitor      = monitor.user.first_name
    last_name_monitor = monitor.user.last_name
    dni_monitor       = monitor.dni
    email             = monitor.user.email
    password1_monitor = ''
    password2_monitor = ''
    password3_monitor = ''
    

    if req.method == "POST":
        name_monitor         = req.POST.get("name-monitor")
        last_name_monitor    = req.POST.get("last-name-monitor")
        dni_monitor          = req.POST.get("dni-monitor")
        email                = req.POST.get("email-monitor").lower()
        password1_monitor    = req.POST.get("password1-monitor")
        password2_monitor    = req.POST.get("password2-monitor")
        password3_monitor    = req.POST.get("password3-monitor")

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_monitor).count() != 0

        if not valid_email:
            show_alert = True
            message = 'El correo no es válido, únicamente correos @utp.edu.co'
        elif email_exists and email != monitor.user.email:
            show_alert = True
            message = 'El correo ya existe'
        elif password2_monitor != '' and password3_monitor != '' and  not(DjangoUser.objects.get(email=email).check_password( password1_monitor )):
            show_alert = True
            message = 'La contraseña actual es incorrecta'
        elif password2_monitor != password3_monitor:
            show_alert = True
            message = 'Las nuevas contraseñas no coinciden'
        elif password1_monitor != '' and password2_monitor == '' and password3_monitor == '':
            show_alert = True
            message = 'Debes ingresar ambas contraseñas para actualizar'
        elif dni_exists and dni_monitor != monitor.dni:
            show_alert = True
            message = 'El documento ya existe'
        else:
            monitor.user.first_name   = name_monitor
            monitor.user.last_name    = last_name_monitor
            monitor.user.username     = email
            monitor.user.email        = email
            monitor.user.save()
            
            if(password2_monitor != '' and password3_monitor != ''):
                userPass = DjangoUser.objects.get(email=email)
                userPass.set_password(password2_monitor)
                userPass.save()

            monitor.dni = dni_monitor
            monitor.save()

            return redirect('/dashboard/monitor/')


    user = SystemUser.objects.get(user=req.user, type_user='Monitor')
    image_profile = user.image_profile

    template = get_template('dashboard/monitors/edit_monitor.html')
    ctx = {
        'email': email,
        'message': message,
        'show_alert': show_alert,
        'id_monitor': id_monitor,
        'dni_monitor': dni_monitor,
        'show_monitor_items': True,
        'name_monitor': name_monitor,
        'image_profile':image_profile,
        'password1_monitor':password1_monitor,
        'password2_monitor':password2_monitor,
        'password3_monitor':password3_monitor,
        'last_name_monitor': last_name_monitor
    }
    return HttpResponse(template.render(ctx, req))
    
# ED7A07D74B8B5C7F0CB04A9BE11B89C886FB73D3