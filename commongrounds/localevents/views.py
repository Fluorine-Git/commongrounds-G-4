from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import EventType, Event

# Create your views here.

def EventListView(request):
    model = EventType
    template_name = "localevents/event_list.html"

def EventDetailView(request, pk):
    model = Event
    template_name = "localevents/event_details.html"