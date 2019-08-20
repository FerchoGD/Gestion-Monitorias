from django.http import HttpResponse
from django.template.loader import get_template
from users.models import User
from core.decorators import UserLogguedDecorator

@UserLogguedDecorator()
def view(req):
    show_alert = False
    message = ''

    if req.method == "POST" and 'delete-admin' in req.POST:
        id_admin = req.POST.get('id_admin')

        admin = User.objects.filter(type_user='Admin', pk=id_admin)
        if admin.count() != 0:
            admin           = admin[0]
            full_name_admin = '%s %s' % (admin.user.first_name, admin.user.last_name)
            admin.user.delete()
            show_alert      = True
            message         = 'El administrador %s fue eliminado' % full_name_admin

    admins = User.objects.filter(type_user='Admin')

    user = User.objects.get(user=req.user)
    image_profile = user.image_profile
    
    template = get_template('dashboard/superuser.html')
    ctx = {
        'show_alert': show_alert,
        'message': message,
        'admins': admins,
        'show_superuser_items': True
    }
    return HttpResponse(template.render(ctx, req))
