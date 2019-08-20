from django.contrib import admin

from .models import RequestUser

@admin.register(RequestUser)
class RequestUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'monitor', 'subject', 'state']
    list_filter = ['user', 'monitor', 'subject', 'state']
