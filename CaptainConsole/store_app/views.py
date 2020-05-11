from django.shortcuts import render, Http404, redirect

from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, ProductImage
from .forms import CheckOutForm


class FrontPageView(TemplateView):
    template_name = 'store_app/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: add front page info, such as top sellers and sales
        return context


class ProductList(ListView):
    model = Product
    template_name = "store_app/productslist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


"""
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
"""




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