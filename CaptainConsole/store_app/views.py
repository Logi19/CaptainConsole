from django.shortcuts import render, Http404

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, ProductImage


class FrontPageView(TemplateView):
    template_name = 'store_app/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: add front page info, such as top sellers and sales
        return context


class ProductList(ListView):
    model = Product
    template_name = "store_app/productslist.html"


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    template_name = "store_app/productslist.html"
    return render(request,template_name, context)


def single_product(request,id):
    try:
        products = Product.objects.get(id=id)
        images = products.productimage_set.all()
        context = {'products': products, 'images': images}
        template_name = "store_app/productDetail.html"
        return render(request,template_name,context)
    except:
        raise Http404




class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: add images from ProductImage (in correct displayOrder)
        context["images"] = None
        return context
