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
    students        = []
    solicitudes     = []

    if req.method == 'POST':
        print(req)
        id_student = req.POST.get('id_student')
        user = SystemUser.objects.get(id=id_student)
        solicitudes = RequestUser.objects.filter(
            user=user,
            state='Accepted',
            requested_time__lte=datetime.now()
        )

    students = SystemUser.objects.filter(type_user='Student')
    user = SystemUser.objects.get(user=req.user, type_user='Admin')
    image_profile = user.image_profile

    template = get_template('dashboard/admins/historial_student.html')
    ctx = {
        'show_alert': show_alert,
        'message': message,
        'show_admins_items': True,
        'id_admin': user.pk,
        'students': students,
        'image_profile':image_profile,
        'solicitudes':solicitudes
    }
    return HttpResponse(template.render(ctx, req))
