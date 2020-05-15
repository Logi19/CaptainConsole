from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
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
        context["todays_deals"] = Product.objects.all()[3:6]
        return context


class ProductList(ListView):
    paginate_by = 24
    queryset = Product.objects.filter(active=True)
    template_name = "store_app/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        manufacturers = [
            m["manufacturer"] for m in Product.objects.values("manufacturer")
        ]
        manufacturer_set = set()
        for manuf in manufacturers:
            manufacturer_set.add((manuf, manuf.replace(" ", "+")))
        context["manufacturers"] = sorted(list(manufacturer_set))
        platforms = [p["platform"] for p in Product.objects.values("platform")]
        platform_set = set()
        for platf in platforms:
            platform_set.add((platf, platf.replace(" ", "+")))
        context["platforms"] = sorted(list(platform_set))
        return context

    def get_queryset(self):
        object_list = self.queryset

        params = dict(self.request.GET.lists())

        if "manufacturer" in params:
            manufacturer_filter = Q(manufacturer__iexact=params["manufacturer"][0])

            if len(params["manufacturer"]) > 1:
                for i in range(1, len(params["manufacturer"])):
                    manufacturer_filter = manufacturer_filter | Q(
                        manufacturer__iexact=params["manufacturer"][i]
                    )

            object_list = object_list.filter(manufacturer_filter)

        if "type" in params:
            type_filter = Q(type__iexact=params["type"][0])

            if len(params["type"]) > 1:
                for i in range(1, len(params["type"])):
                    type_filter = type_filter | Q(type__iexact=params["type"][i])

            object_list = object_list.filter(type_filter)

        if "platform" in params:
            platform_filter = Q(platform__iexact=params["platform"][0])

            if len(params["platform"]) > 1:
                for i in range(1, len(params["platform"])):
                    platform_filter = platform_filter | Q(
                        platform__iexact=params["platform"][i]
                    )

            object_list = object_list.filter(platform_filter)

        if "query" in params:
            query = params["query"]
            object_list = object_list.filter(
                Q(name__icontains=query)
                | Q(manufacturer__icontains=query)
                | Q(platform__icontains=query)
            )

        if "order" in params:
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



def check_number(theinput):
    number = str(theinput)
    if len(number) == 16:
        return True
    elif len(number) == 3:
        return True
    else:
        raise ValidationError(
            ('%(number) is not a valid input'),
            params={'number': number},
        )


def check_String(theinput):
    x = theinput.isalpha()
    if x is True:
        return True
    else:
        raise ValidationError(
            '%(theinput)is not valid',
                                params={'theinput': theinput},
                             )

def combine(month, year):
    expiry_date = str(month) + "-" + str(year)
    return expiry_date


@login_required
def check_out(request):
    """The view function for the checkout process, receives the input from the user
    and validates it before inserting into the database and rendering the next page"""
    print(request.POST)
    if request.method == "POST":
        cardNumber = request.POST.get("cardNumber")
        cardName = request.POST.get("cardName")
        cvc = request.POST.get("cvc")
        month = request.POST.get('month')
        year = request.POST.get('year')
        cardno = check_number(cardNumber)
        cardname = check_String(cardName)
        cvc_card = check_number(cvc)
        expiry_date = combine(month, year)
        print(request.POST.get("cardNumber"))
        print(request.POST.get("cardName"))
        print(request.POST.get("month"))
        print(request.POST.get("year"))
        print(request.POST.get("cvc"))

        form = CheckOutForm(request.POST)

        if form.is_valid():
            if cardno is True and cardname is True and cvc_card is True:
                post = form.save(commit=False)
                post.profile = request.user
                post.orderDiscount = 0
                post.tax = 12
                post.deliveryPrice = 10
                print(type(post))
                post.save()
                return render(
                    request,
                    "shopping_cart_app/order_detail.html",
                    {"post": post, "cardno": cardNumber, "cardname": cardName, "cvc": cvc, 'expiry_date': expiry_date}
                )
            else:
                raise ValidationError(cardno, cardname, cvc_card + "are worng")
        else:
            print("not valid")
            raise ValidationError("WRONG!")
    else:
        form = CheckOutForm()

    return render(request, "store_app/checkouts.html", {"form": form})


def error_404(request, exception):
    data = {}
    return render(request, 'store_app/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'store_app/500.html', data)

def error_403(request, exception):
    data = {}
    return render(request, 'store_app/403.html', data)

def error_400(request, exception):
    data = {}
    return render(request, 'store_app/400.html', data)