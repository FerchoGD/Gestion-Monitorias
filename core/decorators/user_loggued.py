from functools import wraps
from django.conf import settings
from django.shortcuts import redirect

def UserLogguedDecorator(
    # Tipo de usuario loggueado
    type_user='Superuser'
):
    def _ApiValidation(view_func):
        def __apiValidation(request, *args, **kwargs):
            from users.models import User as SystemUser
            if request.user is not None and request.user.is_authenticated:
                user = SystemUser.objects.filter(user=request.user, type_user=type_user)

                if user.count() == 0:
                    # Si no está en el sistema como superusuario
                    return redirect('/logout/')
                pass
            else:
                return redirect('/logout/')

            response = view_func(request, *args, **kwargs)
            return response

        return wraps(view_func)(__apiValidation)
    return _ApiValidation
