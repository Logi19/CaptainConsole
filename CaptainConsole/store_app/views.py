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
from .models import Product, ProductImage, Order, OrderItem, TopSeller
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

        if "search" in params:
            query = params["search"][0]
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
    number = str(theinput.replace(" ", "").replace("-", ""))
    if len(number) == 16:
        return True
    elif len(number) == 3:
        return True
    else:
        raise ValidationError("Invalid card number or CVV")


def check_String(theinput):
    x = theinput.replace(" ", "").isalpha()
    if x is True:
        return True
    else:
        raise ValidationError("Invalid string")


def combine(month, year):
    expiry_date = str(month) + "-" + str(year)
    return expiry_date


@login_required
def check_out(request):
    """
    The view function for the checkout process, receives the input from the user
    and validates it before inserting into the database and rendering the next page.
    """

    if request.method == "POST":
        cardNumber = request.POST.get("cardNumber")
        cardName = request.POST.get("cardName")
        cvc = request.POST.get("cvc")
        month = request.POST.get("month")
        year = request.POST.get("year")
        cardno = check_number(cardNumber)
        cardname = check_String(cardName)
        cvc_card = check_number(cvc)
        expiry_date = combine(month, year)
        form = CheckOutForm(request.POST)

        if form.is_valid():
            if cardno is True and cardname is True and cvc_card is True:
                request.session["deliveryCountry"] = request.POST.get("deliveryCountry")
                request.session["deliveryCity"] = request.POST.get("deliveryCity")
                request.session["deliveryPostal"] = request.POST.get("deliveryPostal")
                request.session["deliveryFirstName"] = request.POST.get(
                    "deliveryFirstName"
                )
                request.session["deliveryLastName"] = request.POST.get(
                    "deliveryLastName"
                )
                request.session["deliveryPhone"] = request.POST.get("deliveryPhone")
                request.session["deliveryCompany"] = request.POST.get("deliveryCompany")
                request.session["deliveryStreet"] = request.POST.get("deliveryStreet")
                request.session["deliveryStreetNum"] = request.POST.get(
                    "deliveryStreetNum"
                )

                request.session["billingFirstName"] = request.POST.get(
                    "billingFirstName"
                )
                request.session["billingLastName"] = request.POST.get("billingLastName")
                request.session["billingPostal"] = request.POST.get("billingPostal")
                request.session["billingCountry"] = request.POST.get("billingCountry")
                request.session["billingCity"] = request.POST.get("billingCity")
                request.session["billingPhone"] = request.POST.get("billingPhone")
                request.session["billingCompany"] = request.POST.get("billingCompany")
                request.session["email"] = request.POST.get("email")
                request.session["billingStreet"] = request.POST.get("billingStreet")
                request.session["billingStreetNum"] = request.POST.get(
                    "billingStreetNum"
                )

                request.session["cardNumber"] = request.POST.get("cardNumber")
                request.session["cardName"] = request.POST.get("cardName")
                request.session["cvc"] = request.POST.get("cvc")

                post = form.save(commit=False)
                post.profile = request.user
                post.orderDiscount = 0
                post.tax = 12
                post.deliveryPrice = 10

                post.deliveryCountry = request.POST.get("deliveryCountry")
                post.save()
                shopping_items = ShoppingCartItem.objects.filter(
                    shoppingCart=request.user.shoppingCart
                )

                return render(
                    request,
                    "shopping_cart_app/order_detail.html",
                    {
                        "post": post,
                        "cardno": cardNumber,
                        "cardname": cardName,
                        "cvc": cvc,
                        "expiry_date": expiry_date,
                        "shopping_items": shopping_items,
                    },
                )
            else:
                raise ValidationError(
                    cardno,
                    cardname,
                    cvc_card + "are not valid, please write valid inputs",
                )
        else:
            print("not valid")
            raise ValidationError("WRONG!")
    else:
        deliveryfirstname = request.session.get("deliveryFirstName")
        deliverylastname = request.session.get("deliveryLastName")
        deliverystreet = request.session.get("deliveryStreet")
        deliverystreetnum = request.session.get("deliveryStreetNum")
        deliverypostal = request.session.get("deliveryPostal")
        deliverycity = request.session.get("deliveryCity")
        deliveryphone = request.session.get("deliveryPhone")
        deliverycompany = request.session.get("deliveryCompany")

        billingfirstname = request.session.get("billingFirstName")
        billinglastname = request.session.get("billingLastName")
        billingstreet = request.session.get("billingStreet")
        billingstreetnum = request.session.get("billingStreetNum")
        billingpostal = request.session.get("billingPostal")
        billingcity = request.session.get("billingCity")
        billingphone = request.session.get("billingPhone")
        billingcompany = request.session.get("billingCompany")
        email = request.session.get("email")

        cvc = request.session.get("cvc")
        cardname = request.session.get("cardName")
        cardnumber = request.session.get("cardNumber")

        form = CheckOutForm(
            {
                "deliveryCity": deliverycity,
                "deliveryPhone": deliveryphone,
                "deliveryPostal": deliverypostal,
                "deliveryStreet": deliverystreet,
                "deliveryCompany": deliverycompany,
                "deliveryFirstName": deliveryfirstname,
                "deliveryLastName": deliverylastname,
                "deliveryStreetNum": deliverystreetnum,
                "billingCity": billingcity,
                "billingPhone": billingphone,
                "billingPostal": billingpostal,
                "billingStreet": billingstreet,
                "billingCompany": billingcompany,
                "billingFirstName": billingfirstname,
                "billingLastName": billinglastname,
                "billingStreetNum": billingstreetnum,
                "cvc": cvc,
                "cardName": cardname,
                "cardNumber": cardnumber,
                "email": email,
            }
        )

    return render(request, "store_app/checkout_page.html", {"form": form})


def error_404(request, exception):
    data = {}
    return render(request, "store_app/404.html", data)


def error_500(request):
    data = {}
    return render(request, "store_app/500.html", data)


def error_403(request, exception):
    data = {}
    return render(request, "store_app/403.html", data)


def error_400(request, exception):
    data = {}
    return render(request, "store_app/400.html", data)
