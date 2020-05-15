from typing import Optional, Any

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse

from .models import ShoppingCart, ShoppingCartItem
from .forms import OrderForm
from .models import ShoppingCartItem

from store_app.models import Order, Product
from profile_app.models import Profile


def my_cart(request, *args, **kwargs):
    context = {}
    shopping_cart = request.user.shoppingCart
    context["cart_key"] = shopping_cart.id
    context["shopping_cart_items"] = ShoppingCartItem.objects.filter(
        shoppingCart=shopping_cart.id
    )
    context["subtotal"] = shopping_cart.get_total_price()
    return render(request, "shopping_cart_app/shopping_cart_detail.html", context)


def remove_from_cart(request, *args, **kwargs):
    data = {}

    shopping_cart_id = request.POST.get("shopping_cart_id")
    product_id = request.POST.get("product_id")

    try:
        item = ShoppingCartItem.objects.get(
            shoppingCart=shopping_cart_id, item=product_id
        )
        item.delete()
        data["message"] = "REMOVED"
    except:
        data["message"] = "ERROR"

    return JsonResponse(data)


class ReceiptView(DetailView):
    model = Order
    template_name = "shopping_cart_app/receipt_view.html"

    def get_object(self):
        profile_id = self.request.session["_auth_user_id"]
        return get_object_or_404(self.model, pk=7)


def receipt_view(request, *args, **kwargs):
    return render(request, "shopping_cart_app/receipt_view.html", context={})


def my_order_detail(request, *args, **kwargs):
    context = {}
    shopping_cart = request.user.shoppingCart
    context["cart_key"] = shopping_cart.id
    context["cart_items"] = ShoppingCartItem.objects.filter(
        shopping_cart=shopping_cart.id
    )
    context["subtotal"] = shopping_cart.get_total_price()
    return render(request, "shopping_cart_app/order_detail.html", context)


class OrderDetail(DetailView):
    model = Order
    template_name = "shopping_cart_app/order_detail.html"

    def get(self, request, *args, **kwargs):
        context = {"pk": 0, "name": "Test"}
        return render(
            request, "shopping_cart_app/order_detail.html", {"context": context}
        )

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return get_object_or_404(Order, pk=pk)

    # def get(self, request, *args, **kwargs):
    #    return render(request, "shopping_cart_app/order_detail.html", {"pk": self.kwargs['pk']})


class OrderCreate(UpdateView):
    model = Profile
    form_class = OrderForm


def add_to_cart(request, *args, **kwargs):
    data = {}

    product_id = request.POST.get("product_id")
    quantity = request.POST.get("quantity")
    if not request.user.is_authenticated:
        data["message"] = "LOGIN NEEDED"
        return JsonResponse(data)
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
