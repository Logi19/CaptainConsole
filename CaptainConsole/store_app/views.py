from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404, redirect
from django.http import JsonResponse

from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

import datetime

from .models import Product, ProductImage, Order, TopSeller
from .forms import CheckOutForm


class FrontPageView(TemplateView):
    template_name = 'store_app/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_sellers = TopSeller.objects.all()[:3]
        context['top_3'] = [Product.objects.get(id=item.product_id) for item in top_sellers]
        context['todays_deals'] = Product.objects.all()[:3]
        return context


class ProductList(ListView):
    paginate_by = 3
    model = Product
    template_name = "store_app/all_productsView.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


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




# class CheckOut(View):
#     def get(self, *args, **kwargs):
#         form = CheckOutForm()
#         return render(self.request, "checkouts.html", {'form': form})
#
#     def post(self, *args, **kwargs):
#         form = CheckOutForm(self.request.POST)
#         print(self.request.POST)
#         if form.is_valid():
#             new_obj = [self.request.id, ]
#             post = form.save(commit=False)
#             post.profile = self.request.user
#             post.processed = 'True'
#             post.items = 2 #Þarf að gera post.items.set(request.id,
#             # fa einhvern veginn öll products ,
#             # setja inn orderDiscount
#             # og setja inn quantity en þetta fer inn i list sem er svo settur hingað inn)
#             post.orderDiscount = 12
#             post.tax = 12
#             post.deliveryPrice = 12
#             post.save()
#             print(post.cleaned_data)
#             print("this works")
#             return redirect("/")
#         return redirect("/cart")

@login_required
def check_out(request):
    print("je")
    if request.method == "POST":
        form = CheckOutForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("ble")
            post = form.save(commit=False)
            # post.save()
            post.deliveryCountry = 'Iceland'
            post.processed = True
            post.profile = request.user
            post.orderDiscount = 0
            post.tax = 12
            post.deliveryPrice = 10
            post.date = datetime.datetime.now()
            post.save()
            return redirect('/')
    else:
        form = CheckOutForm()

    return render(request, 'store_app/checkouts.html', {'form': form})
