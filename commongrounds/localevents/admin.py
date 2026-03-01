from django.contrib import admin
from .models import EventType, Event

# Register your models here.

class EventTypeAdmin(admin.ModelAdmin):
    model = EventType

class EventAdmin(admin.ModelAdmin):
    model = EventType

admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
