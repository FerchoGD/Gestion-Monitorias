from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'type_user',]
    list_filter = ['type_user',]
