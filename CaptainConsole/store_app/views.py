from django.shortcuts import render, Http404, redirect

from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, ProductImage, TopSeller
from .forms import CheckOutForm


class FrontPageView(TemplateView):
    template_name = 'store_app/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_sellers = TopSeller.objects.all()[:3]
        context['top_3'] = [Product.objects.get(id=item.product_id) for item in top_sellers]
        return context


class ProductList(ListView):
    model = Product
    template_name = "store_app/productslist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = "store_app/productDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image_objects = list(self.object.get_images())
        image_objects.sort()
        images = [img.image.name for img in image_objects]
        context["images"] = images
        return context


class CheckOut(View):
    def get(self, *args, **kwargs):
        form = CheckOutForm()
        context = {
            'form': form,
        }
        return render(self.request, "order_form.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print("this works")
            return redirect("/")