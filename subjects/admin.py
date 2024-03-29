from django.contrib import admin

from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'name',]
    list_filter = ['code',]
