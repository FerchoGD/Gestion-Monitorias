from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



from users.models import User as SystemUser
from subjects.models import Subject
from requests_users.models import RequestUser

@UserLogguedDecorator(type_user='Monitor')
def view(req):
    show_alert          = False
    message             = ''

    user = SystemUser.objects.get(user=req.user, type_user='Monitor')
    image_profile = user.image_profile

    from datetime import datetime

    solicitudes = RequestUser.objects.filter(
        monitor=user,
        state='Accepted'
    )

    if req.method == 'POST' and 'accept' in req.POST:
        id_solicitude = req.POST.get('id_solicitude')
        solicitude = RequestUser.objects.get(pk=id_solicitude)
        solicitude.state = 'FinishedMonitor'
        solicitude.save()
        email_monitor = user.user.email
        estudiante = solicitude.user.user.first_name
        email_estudiante = solicitude.user.user.email
        monitor = solicitude.monitor.user.first_name
        asignatura = solicitude.subject.name
        fecha = solicitude.requested_time
        message = "Por favor confirme si la monitoria si se tomo y fue finalizada, esto lo pude realizar desde su perfil."

        body = render_to_string(
            'dashboard/monitors/email_content_finish.html', {
                'estudiante': estudiante,
                'email': email_monitor,
                'monitor': monitor,
                'asignatura': asignatura,
                'fecha': fecha,
                'message': message,
            },
        )

        email_message = EmailMessage(
            subject='Monitoria finalizada',
            body=body,
            to=[email_estudiante],
        )
        email_message.content_subtype = 'html'
        email_message.send()

    template = get_template('dashboard/monitors/solicitudes.html')
    ctx = {
        'message': message,
        'id_monitor': user.pk,
        'show_alert': show_alert,
        'show_monitor_items': True,
        'solicitudes': solicitudes,
        'image_profile':image_profile,
        'solicitud_list':True
    }
    return HttpResponse(template.render(ctx, req))
