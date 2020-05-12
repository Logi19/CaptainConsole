from typing import Optional, Any

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .models import ShoppingCart
from .forms import OrderForm

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
    items = ShoppingCart.objects.get(pk=cart_id).items.all()
    current_item = items.get(id=product_id)
    print(current_item)
    current_item.delete()
    return HttpResponseRedirect(reverse("shoppingcart_detail", kwargs={'pk': cart_id}))

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    #context["shopping_cart_list"] = ShoppingCart.objects.all()
    #    context["shopping_cart_list"] = ShoppingCart.objects.get(pk=self.kwargs['pk']).items.all()
    #    print("Context: {}".format(ShoppingCart.objects.get(pk=1).items.all()))
    #    return context

    # def get(self, request, *args, **kwargs):
    #    #for item in ShoppingCart.objects.get(pk=1).items.all():
    #    #    print(item.get_thumbnail())
    #    context = dict(items=[dict(name="Mario", developer="Genesis Game", price=12.99),
    #                          dict(name="Sonic The HedgeHog", developer="Genesis Game", price=20.99),
    #                          dict(name="Nintendo Entertainment System Console", developer="NES", price=30.99)])

    #    return render(request, "shopping_cart_app/shopping_cart_detail.html", context=context)


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
