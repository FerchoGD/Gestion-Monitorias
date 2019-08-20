from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from datetime import datetime

from users.models import User as SystemUser
from subjects.models import Subject
from requests_users.models import RequestUser
from schedules.models import TimeSlot, DAYS

@UserLogguedDecorator(type_user='Monitor')
def view(req):
    show_alert          = False
    message             = ''

    user = SystemUser.objects.get(user=req.user, type_user='Monitor')
    image_profile = user.image_profile
    slots_user = TimeSlot.objects.filter(user=user, type='Calendar')

    if req.method == 'POST':
        data_schedule = req.POST.get('data_schedule').split(',')
        slots_user.delete()
        DAYS_DATA = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado']

        for data_row in data_schedule:
            hour, day   = data_row.split('-')
            hour        = int(hour)
            day         = DAYS_DATA[int(day) - 1]
            next_hour   = hour + 1

            hour = datetime.now().replace(
                hour=hour,
                minute=0,
                second=0,
                microsecond=0
            )

            next_hour = datetime.now().replace(
                hour=next_hour,
                minute=0,
                second=0,
                microsecond=0
            )

            new_slot = TimeSlot(
                user=user,
                start_time=hour,
                end_time=next_hour,
                day=day,
                type='Calendar'
            )
            new_slot.save()

            show_alert  = True
            message     = 'Horario actualizado'

    slots_user = TimeSlot.objects.filter(user=user, type='Calendar')
    data = range(7, 23)
    slots = []
    for slot in slots_user:
        hour = slot.start_time.hour
        day = DAYS.index((slot.day, slot.day)) + 1
        id_on_html = '%i-%i' % (hour, day)
        slots.append(id_on_html)

    template = get_template('dashboard/monitors/calendar.html')
    ctx = {
        'data': data,
        'slots': slots,
        'message': message,
        'id_monitor': user.pk,
        'show_alert': show_alert,
        'show_monitor_items': True,
        'image_profile':image_profile

    }
    return HttpResponse(template.render(ctx, req))
