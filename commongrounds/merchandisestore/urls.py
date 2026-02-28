from django.urls import path
from .views import (
    MerchandiseStoreListView,
    MerchandiseStoreDetailView,
)

app_name = 'merchandisestore'
urlpatterns = [
    path('items/', MerchandiseStoreListView.as_view(),
         name='merchandisestore-list'),
    path('item/<int:id>/', MerchandiseStoreDetailView.as_view(),
         name='merchandisestore-detail'),
]
