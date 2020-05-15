from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404, redirect
from django.http import JsonResponse
from django.db.models import Q

from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse

import datetime
import json

from shopping_cart_app.models import ShoppingCart, ShoppingCartItem
from .models import Product, ProductImage, Order, TopSeller
from .forms import CheckOutForm


class FrontPageView(TemplateView):
    template_name = "store_app/frontpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_sellers = TopSeller.objects.all()[:3]
        context["top_3"] = [Product.objects.get(id=item.id) for item in top_sellers]
        context["todays_deals"] = Product.objects.all()[:3]
        return context



class ProductList(ListView):
    paginate_by = 24
    queryset = Product.objects.filter(active=True)
    template_name = "store_app/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manufacturers = [m['manufacturer'] for m in Product.objects.values('manufacturer')]
        manufacturer_set = set()
        for manuf in manufacturers:
            manufacturer_set.add((manuf, manuf.replace(' ', '+')))
        context['manufacturers'] = sorted(list(manufacturer_set))
        platforms = [p['platform'] for p in Product.objects.values('platform')]
        platform_set = set()
        for platf in platforms:
            platform_set.add((platf, platf.replace(' ', '+')))
        context['platforms'] = sorted(list(platform_set))
        return context

    def get_queryset(self):
        object_list = self.queryset

        params = dict(self.request.GET.lists())

        if 'manufacturer' in params:
            manufacturer_filter = Q(manufacturer__iexact=params['manufacturer'][0])

            if len(params['manufacturer']) > 1:
                for i in range(1, len(params['manufacturer'])):
                    manufacturer_filter = manufacturer_filter | Q(manufacturer__iexact=params['manufacturer'][i])

            object_list = object_list.filter(manufacturer_filter)

        if 'type' in params:
            type_filter = Q(type__iexact=params['type'][0])

            if len(params['type']) > 1:
                for i in range(1, len(params['type'])):
                    type_filter = type_filter | Q(type__iexact=params['type'][i])

            object_list = object_list.filter(type_filter)

        if 'platform' in params:
            platform_filter = Q(platform__iexact=params['platform'][0])

            if len(params['platform']) > 1:
                for i in range(1, len(params['platform'])):
                    platform_filter = platform_filter | Q(platform__iexact=params['platform'][i])

            object_list = object_list.filter(platform_filter)


        if 'query' in params:
            query = params['query']
            object_list = object_list.filter(
                Q(name__icontains=query)
                | Q(manufacturer__icontains=query)
                | Q(platform__icontains=query)
            )

        if 'order' in params:
            order_by = params["order"][0]

            if order_by == "year-asc":
                object_list = object_list.order_by("year")
            elif order_by == "year-desc":
                object_list = object_list.order_by("-year")
            elif order_by == "price-asc":
                object_list = object_list.order_by("price")
            elif order_by == "price-desc":
                object_list = object_list.order_by("-price")
            elif order_by == "name-asc":
                object_list = object_list.order_by("-name")
            elif order_by == "name-desc":
                object_list = object_list.order_by("name")

        return object_list


class ProductDetail(DetailView):
    model = Product
    template_name = "store_app/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        image_objects = list(self.object.get_images())
        image_objects.sort(key=lambda x: x.displayOrder)
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

def check_number(number):
    theNumber = str(number)
    lennumber = len(theNumber)
    x = theNumber.isdigit()
    if lennumber == 16 and x is True:
        return True
    elif lennumber == 3 and x is True:
        return True
    else:
        return False

def check_String(strings):
    x = strings.isalpha()
    if x is True:
        return True
    else:
        return False

# def check_date(string):
#


@login_required
def check_out(request):
    print(request.POST.get("cardNumber"))

    # cardno = check_number(request.POST.get('cardNumber', None))
    # cardname = check_String(request.POST.get('cardName', None))
    # cvc_card = check_number(request.GET.get('cvc', None))
    # expiryDate = check_date(request.POST.get('expiryDate'))

    if request.method == "POST":
        form = CheckOutForm(request.POST)

        if form.is_valid():
            # cardno = check_number(request.POST.get('cardNumber'))
            # cardname = check_String(request.POST.get('cardName'))
            # cvc_card = check_number(request.POST.get('cvc'))
            # # expiryDate = check_date(request.POST.get('expiryDate'))
            # # if cardno == True and cardname == True
            # #     and cvc_card is True and expiryDate == True:
            post = form.save(commit=False)
            # post.save()
            post.deliveryCountry = "Iceland"
            post.processed = True
            post.profile = request.user
            post.orderDiscount = 0
            post.tax = 12
            post.deliveryPrice = 10
            cardName = request.POST.get('cardName')
            cardNumber = request.POST.get('cardNumber')
            expirydate = request.POST.get('expiryDate')
            cvc = request.POST.get('cvc')
            post.save()

            return render(request, 'shopping_cart_app/order_detail.html', {'post': post,
                                                                            'cardno': cardNumber,
                                                                            'cardname': cardName,
                                                                            'cvc': cvc,
                                                                            'expirydate': expirydate
                                                                           })
        else:
            form = CheckOutForm
    else:
        form = CheckOutForm()

    return render(request, "store_app/checkouts.html", {"form": form})


def add_to_cart(request, *args, **kwargs):
    data = {}

    product_id = request.POST.get("product_id")
    quantity = request.POST.get("quantity")
    shopping_cart_id = request.user.shoppingCart.id

    in_cart_item = ShoppingCartItem.objects.filter(
        shoppingCart=shopping_cart_id, item=product_id
    )

    if len(in_cart_item) > 0:
        if in_cart_item[0].quantity + quantity <= 32767:
            in_cart_item[0].quantity += quantity
            in_cart_item[0].save()

            data["message"] = "Item quantity updated."
            return JsonResponse(data)
    else:
        cart_item = ShoppingCartItem()
        cart_item.item = Product.objects.get(id=product_id)
        cart_item.shoppingCart = ShoppingCart.objects.get(id=shopping_cart_id)
        cart_item.quantity = int(quantity)

        cart_item.save()
        data["message"] = "Item successfully added to cart."
        return JsonResponse(data)

    data["message"] = "Something went wrong."
    return JsonResponse(data)
