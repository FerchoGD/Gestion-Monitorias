from django.http import HttpResponse
from django.template.loader import get_template

from users.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def view(req):
    show_alert = False
    message = ''

    template = get_template('inicio/inicio.html')
    ctx = {
        'showAlert': show_alert,
        'message': message,
        'inicio':True,
    }

    return HttpResponse(template.render(ctx, req))
