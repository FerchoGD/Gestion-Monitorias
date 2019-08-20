from django.http import HttpResponse
from django.template.loader import get_template

from users.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def view(req):
    show_alert = False
    message = ''
    email=''

    if req.method == 'POST':
        email = req.POST.get('email').lower()
        password = req.POST.get('password')

        user = authenticate(username=email, password=password)

        if user:
            system_user = User.objects.filter(user=user)
            if system_user.count() == 0:
                show_alert = True
                message = 'El usuario no existe'
            else:
                system_user = system_user[0]
                type_user = system_user.type_user
                print(type_user)

                login(req, user)
                if type_user == 'Superuser':
                    return redirect('/dashboard/superuser/')
                elif type_user == 'Admin':
                    return redirect('/dashboard/admin/')
                elif type_user == 'Student':
                    return redirect('/dashboard/student/historial/')
                elif type_user == 'Monitor':
                    return redirect('/dashboard/monitor/')
        else:
            show_alert = True
            message = 'El usuario no existe'

    template = get_template('login/login.html')
    ctx = {
        'showAlert': show_alert,
        'message': message,
        'email':email
    }

    return HttpResponse(template.render(ctx, req))
