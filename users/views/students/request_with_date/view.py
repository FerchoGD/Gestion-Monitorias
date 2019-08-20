from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect
from core.decorators import UserLogguedDecorator

from datetime import datetime, timedelta

from users.models import User as SystemUser
from requests_users.models import RequestUser
from subjects.models import Subject
from schedules.models import TimeSlot, DAYS

@UserLogguedDecorator(type_user='Student')
def view(req, id_subject, id_monitor):
    show_alert      = False
    message         = ''
    subject = Subject.objects.filter(pk=id_subject)
    monitor = SystemUser.objects.filter(pk=id_monitor)
    user = SystemUser.objects.get(user=req.user, type_user='Student')
    image_profile = user.image_profile

    if subject.count == 0 or monitor.count() == 0:
        return redirect('/dashboard/student/historial/')

    subject = subject[0]
    monitor = monitor[0]

    if req.method == 'POST':
        id_slot_selected    = int(req.POST.get('id_slot_selected'))
        weekday             = int(req.POST.get('weekday'))

        today = datetime.today()
        today_weekday = today.weekday() + 1
        additional_days = 0
        if today_weekday == weekday:
            additional_days = 6
        elif weekday < today_weekday:
            additional_days = 6 - today_weekday + weekday
        else:
            additional_days = today_weekday - weekday
        requested_time = today + timedelta(days=additional_days)

        time_slot = TimeSlot.objects.get(id=id_slot_selected)
        time_slot.pk = None
        time_slot.type = 'Calendar'
        time_slot.user = user
        time_slot.save()

        request_user = RequestUser(
            user=user,
            monitor=monitor,
            requested_time=requested_time,
            time_slot=time_slot,
            subject=subject,
            state='Requested'
        )
        request_user.save()
        return redirect('/dashboard/student/historial/')

    subjects = Subject.objects.all()

    calendar_slots = TimeSlot.objects.filter(user=monitor, type='Calendar')
    data = range(7, 23)
    slots = []
    for slot in calendar_slots:
        hour = slot.start_time.hour
        day = DAYS.index((slot.day, slot.day)) + 1
        id_on_html = '%i-%i' % (hour, day)
        slots.append((id_on_html, slot.pk))

    template = get_template('dashboard/students/calendar.html')
    ctx = {
        'data': data,
        'slots': slots,
        'message': message,
        'id_student': user.pk,
        'show_alert': show_alert,
        'show_students_items': True,
        'image_profile':image_profile
    }
    return HttpResponse(template.render(ctx, req))
