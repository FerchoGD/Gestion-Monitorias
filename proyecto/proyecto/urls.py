from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from account.urls import account_patterns


urlpatterns = [

    path('',include('core.urls')),
    path('account/',include(account_patterns)),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)