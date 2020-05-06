from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product


class FrontPageView(TemplateView):
    template_name = 'store_app/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: add front page info, such as top sellers and sales
        return context


class ProductList(ListView):
    model = Product
    template_name = "store_app/productslist.html"


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: add images from ProductImage (in correct displayOrder)
        context["images"] = None
        return context
