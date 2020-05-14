from typing import Optional, Any

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse

from .models import ShoppingCart
from .forms import OrderForm
from .models import ShoppingCartItem

from store_app.models import Order
from profile_app.models import Profile



def my_cart(request, *args, **kwargs):
    context = {}
    shopping_cart = request.user.shoppingCart
    context['cart_key'] = shopping_cart.id
    context['shopping_cart_items'] = ShoppingCartItem.objects.filter(shoppingCart=shopping_cart.id)
    context['subtotal'] = shopping_cart.get_total_price()
    return render(request, 'shopping_cart_app/shopping_cart_detail.html', context)


def remove_from_cart(request,  *args, **kwargs):
    data = {}

    shopping_cart_id = request.POST.get('shopping_cart_id')
    product_id = request.POST.get('product_id')

    item = ShoppingCartItem.objects.get(shoppingCart=shopping_cart_id, item=product_id)
    item.delete()

    return JsonResponse(data)


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
