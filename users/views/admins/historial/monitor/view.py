from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from datetime import datetime
from users.models import User as SystemUser
from requests_users.models import RequestUser
from subjects.models import Subject

@UserLogguedDecorator(type_user='Admin')
def view(req):
    show_alert      = False
    message         = ''
    monitors        = []
    solicitudes     = []
    modal_horas     = False
    num_horas       = 0

    if req.method == 'POST':
        modal_horas = True
        id_monitor = req.POST.get('id_monitor')
        monitor = SystemUser.objects.get(id=id_monitor)
        solicitudes = RequestUser.objects.filter(
            monitor=monitor,
            state='Accepted',
            requested_time__lte=datetime.now()
        )
        num_horas = solicitudes.count()

    monitors = SystemUser.objects.filter(type_user='Monitor')
    user = SystemUser.objects.get(user=req.user, type_user='Admin')
    image_profile = user.image_profile

    template = get_template('dashboard/admins/historial_monitor.html')
    ctx = {
        'show_alert': show_alert,
        'message': message,
        'show_admins_items': True,
        'id_admin': user.pk,
        'monitors': monitors,
        'image_profile':image_profile,
        'solicitudes':solicitudes,
        'modal_horas':modal_horas,
        'horas_totales':num_horas
    }
    return HttpResponse(template.render(ctx, req))
