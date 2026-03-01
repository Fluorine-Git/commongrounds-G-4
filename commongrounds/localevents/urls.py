from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>', EventDetailView.as_view(), name='event_details'),
]

app_name = "localevents"