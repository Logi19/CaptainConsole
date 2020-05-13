from typing import Optional, Any

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import ShoppingCart
from .forms import OrderForm
from .models import ShoppingCartItem

from store_app.models import Order
from profile_app.models import Profile


class ShoppingCartDetail(DetailView):
    model = ShoppingCart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_key = self.kwargs['pk']
        context['cart_key'] = cart_key
        items = ShoppingCart.objects.get(pk=cart_key).items.all()
        context['shopping_cart_items'] = items
        context['subtotal'] = sum([item.price for item in items])
        return context


def remove_from_cart(request, product_id, cart_id):
    current_cart = ShoppingCartItem.objects.filter(shoppingCart=cart_id)
    current_item = current_cart.filter(item_id=product_id)
    current_item.delete()
    return HttpResponseRedirect(reverse("shoppingcart_detail", kwargs={'pk': cart_id}))

class ReceiptView(DetailView):
    model = Order


class OrderDetail(DetailView):
    model = Order
    template_name = "shopping_cart_app/order_detail.html"

    def get(self, request, *args, **kwargs):
        context = {
            'pk': 0,
            'name': 'Test'
        }
        return render(request, "shopping_cart_app/order_detail.html", {"context": context})

    # def get_object(self):
    #    pk = self.kwargs.get('pk')
    #    return get_object_or_404(Order, pk=pk)

    # def get(self, request, *args, **kwargs):
    #    return render(request, "shopping_cart_app/order_detail.html", {"pk": self.kwargs['pk']})


class OrderCreate(UpdateView):
    model = Profile
    form_class = OrderForm
