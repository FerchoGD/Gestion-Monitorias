from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from users.models import User as SystemUser
from subjects.models import Subject

@UserLogguedDecorator(type_user='Monitor')
def view(req):
    show_alert          = False
    message             = ''

    user = SystemUser.objects.get(user=req.user, type_user='Monitor')
    image_profile = user.image_profile

    template = get_template('dashboard/admins/dashboard.html')
    ctx = {
        'message': message,
        'id_monitor': user.pk,
        'show_alert': show_alert,
        'show_monitor_items': True,
        'image_profile':image_profile
    }
    return HttpResponse(template.render(ctx, req))
