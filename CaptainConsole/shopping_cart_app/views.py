from typing import Optional, Any

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse

from .models import ShoppingCart, ShoppingCartItem
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


def receipt_view(request, *args, **kwargs):
    """
        View that will be displayed after the order has been place.
        The function clears out the shopping cart for the user
        and marks the order as processed.
    """
    shopping_cart = request.user.shoppingCart
    for item in ShoppingCartItem.objects.filter(shoppingCart=shopping_cart):
        item.delete()
    request.user.order_set.filter(processed=False).update(processed=True)
    return render(request, "shopping_cart_app/receipt_view.html", context={})


def my_order_detail(request, *args, **kwargs):
    return render(request, "shopping_cart_app/order_detail.html", {})

def add_to_cart(request, *args, **kwargs):
    data = {}

    product_id = request.POST.get("product_id")
    quantity = int(request.POST.get("quantity"))
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
