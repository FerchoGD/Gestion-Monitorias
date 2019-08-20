from django.contrib import admin

from .models import TimeSlot

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['user', 'type',]
    list_filter = ['user', 'type',]
