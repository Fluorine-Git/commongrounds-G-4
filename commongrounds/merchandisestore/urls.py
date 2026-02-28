from django.urls import path
from .views import (
    MerchandiseStoreListView,
    # MerchandiseDetailView,
)

app_name = 'merchandisestore'
urlpatterns = [
    path('items/', MerchandiseStoreListView.as_view(),
         name='merchandisestore-list'),
    # path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
]
