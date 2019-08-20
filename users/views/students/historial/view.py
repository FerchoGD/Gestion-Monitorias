from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from users.models import User as SystemUser
from requests_users.models import RequestUser

@UserLogguedDecorator(type_user='Student')
def view(req):
    show_alert          = False
    message             = ''

    user = SystemUser.objects.get(user=req.user, type_user='Student')
    image_profile = user.image_profile

    solicitudes = RequestUser.objects.filter(user=user).exclude(state='Declined').order_by('state')

    if req.method == 'POST' and 'finalice' in req.POST:
        id_solicitude = req.POST.get('id_solicitude')
        solicitude = RequestUser.objects.get(pk=id_solicitude)
        solicitude.state = 'FinishedEstudent'
        solicitude.save()

    template = get_template('dashboard/students/historial.html')
    ctx = {
        'message': message,
        'id_student': user.pk,
        'show_alert': show_alert,
        'solicitudes': solicitudes,
        'show_students_items': True,
        'image_profile':image_profile
    }
    return HttpResponse(template.render(ctx, req))
