from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    ListView,
    # DetailView,
)
from .models import Product, ProductType


class MerchandiseStoreListView(ListView):
    template_name = 'merchandisestore/merchandisestore_list.html'
    queryset = Product.objects.all()  # blog/<modelname>_list.html


# class MerchandiseDetailView(DetailView):
#     template_name = 'merchandisestore/merchandisestore_detail.html'
#     # queryset = Article.objects.all()

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Product, id=id_)
