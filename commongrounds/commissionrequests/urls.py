from django.urls import path
from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name='list_view'),
    path('commissions/request/<int:pk>', detail_view, name='detail_view'),
] 

app_name = 'commissionrequests'