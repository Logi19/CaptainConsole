from django.shortcuts import render
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
        context["shopping_cart_list"] = ShoppingCart.objects.all()
        return context


class ReceiptView(DetailView):
    model = Order


class OrderDetail(DetailView):
    model = Order

    def get(self, request, *args, **kwargs):
        return render(request, "shopping_cart_app/order_detail.html", {"pk": self.kwargs['pk']})


class OrderCreate(UpdateView):
    model = Profile
    form_class = OrderForm
