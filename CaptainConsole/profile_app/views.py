from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages
from django.http import JsonResponse

from store_app.models import Product, Order, OrderItem
from .models import Profile, SearchHistory
from .forms import ProfileForm
from .forms import SignUpForm


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/store/")
            else:
                return HttpResponse("Your account is inactive.")
        else:
            print(f"Failed login attempt with email: {email}")
            return HttpResponse("Invalid login details given")
    else:
        return render(request, "profile_app/log_in.html")


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect("/store/")


@login_required
def my_profile_view(request, *args, **kwargs):
    context = {"user": request.user}
    order_list = list(Order.objects.filter(profile_id=request.user.id))
    order_list.sort(key=lambda x: x.date, reverse=True)
    order_item_list = []
    for order in order_list:
        order_item_list.append((order, list(OrderItem.objects.filter(order=order.id))))
    context["order_history"] = order_item_list
    return render(request, "profile_app/view_profile.html", context)


@login_required
def my_profile_update(request, *args, **kwargs):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_first_name = request.POST.get("first_name")
            new_last_name = request.POST.get("last_name")
            if "profileImage" in request.FILES:
                new_profile_image = request.FILES["profileImage"]
            else:
                new_profile_image = None

            profile = Profile.objects.get(id=request.user.id)

            profile.first_name = new_first_name
            profile.last_name = new_last_name
            if new_profile_image is not None:
                profile.profileImage = new_profile_image

            profile.save()
            messages.success(request, "Profile successfully updated!")
            return HttpResponseRedirect("")
    else:
        data = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }
        form = ProfileForm(initial=data)
        context = {
            "user": request.user,
            "form": form,
            "messages": get_messages(request),
        }
        return render(request, "profile_app/edit_profile.html", context)


def sign_up_view(request, *args, **kwargs):
    if request.method == "POST":

        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return HttpResponseRedirect("/store/")

    else:
        form = SignUpForm()
    return render(request, "profile_app/sign_up.html", {"form": form})


def my_profile_search_hist(request, *args, **kwargs):
    context = {"user": request.user}
    search_hist = list(SearchHistory.objects.filter(searchProfile=request.user.id))
    search_hist.sort(key=lambda x: x.time, reverse=True)
    context["search_history"] = search_hist
    return render(request, "profile_app/search_history.html", context)


def add_to_search_history(request, *args, **kwargs):
    """
    Receives an AJAX request and adds a product to the user's search history,
    if it isn't the latest item in their search history.
    """
    data = {}

    profile_id = request.POST.get("profile_id")
    product_id = request.POST.get("product_id")

    if profile_id is not None and product_id is not None:
        product = Product.objects.get(id=product_id)
        profile = Profile.objects.get(id=profile_id)
        last_search = SearchHistory.objects.filter(searchProfile=profile).order_by("-time")[0]

        if last_search.searchProduct != product:
            search = SearchHistory()
            search.searchProduct = product
            search.searchProfile = profile
            search.save()
            data["message"] = "ADDED"
            return JsonResponse(data)
        else:
            data["message"] = "NOT ADDED"
            return JsonResponse(data)

    data["message"] = "ERROR"
    return JsonResponse(data)
