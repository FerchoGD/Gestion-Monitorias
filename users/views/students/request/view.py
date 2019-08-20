from django.http import HttpResponse
from django.template.loader import get_template
from core.decorators import UserLogguedDecorator

from users.models import User as SystemUser
from requests_users.models import RequestUser
from subjects.models import Subject

@UserLogguedDecorator(type_user='Student')
def view(req):
    show_alert      = False
    message         = ''
    monitors        = []
    id_subject      = 0

    if req.method == 'POST':
        id_subject = req.POST.get('id_subject')
        subject = Subject.objects.get(pk=id_subject)
        monitors = SystemUser.objects.filter(subject_assigned=subject)

    user = SystemUser.objects.get(user=req.user, type_user='Student')
    image_profile = user.image_profile
    subjects = Subject.objects.all()

    template = get_template('dashboard/students/request_search.html')
    ctx = {
        'message': message,
        'subjects': subjects,
        'monitors': monitors,
        'id_student': user.pk,
        'show_alert': show_alert,
        'id_subject': id_subject,
        'show_students_items': True,
        'image_profile':image_profile

    }
    return HttpResponse(template.render(ctx, req))
