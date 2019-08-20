from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from users.models import User as SystemUser
from subjects.models import Subject

@UserLogguedDecorator(type_user='Admin')
def view(req):
    show_alert              = False
    editting_monitor        = False
    message                 = ''

    id_monitor_editting     = 0
    name_monitor            = ''
    last_name_monitor       = ''
    dni_monitor             = ''
    email                   = ''
    password                = ''
    gender                  = ''
    fecha_nacimiento_monitor= ''
    horas_por_cumplir       =''

    if req.method == "POST" and 'delete-monitor' in req.POST:
        id_monitor = req.POST.get("id_monitor")
        user = SystemUser.objects.filter(pk=id_monitor)

        if user.count() != 0:
            user = user[0]
            user.user.delete()

    elif req.method == "POST" and 'create-monitor-submit' in req.POST:
        name_monitor = req.POST.get("name-monitor")
        last_name_monitor = req.POST.get("last-name-monitor")
        dni_monitor = req.POST.get("dni-monitor")
        email = req.POST.get("email-monitor").lower()
        password_monitor = req.POST.get("password-monitor")
        subjects = req.POST.getlist("subjects")
        birth_date = req.POST.get("fecha-nacimiento-monitor")
        gender = req.POST.get("gender")
        horas_por_cumplir = req.POST.get("hours")

        from django.contrib.auth.models import User as DjangoUser

        valid_email     = email.endswith('@utp.edu.co')
        email_exists    = DjangoUser.objects.filter(email=email).count() != 0
        dni_exists      = SystemUser.objects.filter(dni=dni_monitor).count() != 0

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
                first_name=name_monitor,
                last_name=last_name_monitor,
                password=password_monitor,
                email=email
            )
            django_user.save()
            django_user.set_password(password_monitor)
            django_user.save()

            system_user = SystemUser(
                user=django_user,
                type_user='Monitor',
                dni=dni_monitor,
                birth_date=birth_date,
                gender=gender,
                hours=horas_por_cumplir
            )
            system_user.save()

            for id_subject in subjects:
                subject = Subject.objects.filter(pk=id_subject)
                if subject.count() != 0:
                    subject = subject[0]
                    system_user.subject_assigned.add(subject)

            system_user.save()
    elif req.method == "POST" and 'get-info-monitor' in req.POST:
        id_monitor_editting = req.POST.get("id_monitor")
        user = SystemUser.objects.filter(pk=id_monitor_editting)

        if user.count() != 0:
            user = user[0]
            name_monitor                = user.user.first_name
            last_name_monitor           = user.user.last_name
            dni_monitor                 = user.dni
            email                       = user.user.email
            gender                      = user.gender
            fecha_nacimiento_monitor    = user.birth_date
            horas_por_cumplir           = user.hours
            editting_monitor    = True
    elif req.method == "POST" and 'edit-monitor-submit' in req.POST:
        id_monitor = req.POST.get("id_monitor")

        monitor = SystemUser.objects.get(pk=id_monitor)

        name_monitor = req.POST.get("name-monitor")
        last_name_monitor = req.POST.get("last-name-monitor")
        dni_monitor = req.POST.get("dni-monitor")
        email = req.POST.get("email-monitor").lower()
        subjects = req.POST.getlist("subjects")
        birth_date = req.POST.get("fecha-nacimiento-monitor")
        gender = req.POST.get("gender")
        horas_por_cumplir = req.POST.get("hours")

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
        elif dni_exists and dni_monitor != monitor.dni:
            show_alert = True
            message = 'El documento ya existe'
        else:
            monitor.user.username=email
            monitor.user.first_name=name_monitor
            monitor.user.last_name=last_name_monitor
            monitor.user.email=email
            monitor.user.save()

            monitor.dni=dni_monitor
            monitor.birth_date=birth_date
            monitor.gender=gender
            if(horas_por_cumplir != ''):
                monitor.hours=horas_por_cumplir
            monitor.subject_assigned.clear()
            monitor.save()

            for id_subject in subjects:
                subject = Subject.objects.filter(pk=id_subject)
                if subject.count() != 0:
                    subject = subject[0]
                    monitor.subject_assigned.add(subject)

            monitor.save()

    monitors = SystemUser.objects.filter(type_user='Monitor')
    subjects = Subject.objects.all()
    genders = ['Masculino','Femenino']

    user = SystemUser.objects.get(user=req.user, type_user='Admin')
    image_profile = user.image_profile
    template = get_template('dashboard/admins/dashboard.html')
    ctx = {
        'show_alert': show_alert,
        'message': message,
        'monitors': monitors,
        'show_admins_items': True,
        'name_monitor': name_monitor,
        'last_name_monitor': last_name_monitor,
        'dni_monitor': dni_monitor,
        'email': email,
        'subjects': subjects,
        'genders': genders,
        'editting_monitor': editting_monitor,
        'id_monitor_editting': id_monitor_editting,
        'id_admin': user.pk,
        'image_profile':image_profile,
        'horas_por_cumplir':horas_por_cumplir,
        'fecha_nacimiento_monitor':fecha_nacimiento_monitor,
        'genero':gender
    }
    return HttpResponse(template.render(ctx, req))
