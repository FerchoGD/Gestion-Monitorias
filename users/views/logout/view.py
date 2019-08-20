from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth import logout

def view(req):
    logout(req)
    return redirect('/login/')
